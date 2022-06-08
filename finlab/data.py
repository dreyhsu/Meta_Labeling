# -*- coding: utf-8 -*-
import os
import pandas as pd
import datetime
import numpy as np
from talib import abstract
from .crawler import check_monthly_revenue

class Data():
    
    
    def __init__(self):
        
        self.date = datetime.datetime.now().date()
        self.warrning = False
        
        self.col2table = {}
        tnames = os.listdir(os.path.join('history', 'items'))
        
        for tname in tnames:
            
            path = os.path.join('history', 'items', tname)
            
            if not os.path.isdir(path):
                continue
                            
            items = [f[:-4] for f in os.listdir(path)]
            for item in items:
                if item not in self.col2table:
                    self.col2table[item] = []
                self.col2table[item].append(tname)
    
    def get(self, name, amount=0, table=None, convert_to_numeric=True):
        if table is None:
            candidates = self.col2table[name]
            if len(candidates) > 1 and self.warrning:
                print('**WARRN there are tables have the same item', name, ':', candidates)
                print('**      take', candidates[0])
                print('**      please specify the table name as an argument if you need the file from another table')
                for c in candidates:
                    print('**      data.get(', name, ',',amount, ', table=', c, ')')
                    
            table = candidates[0]
            
        df = pd.read_pickle(os.path.join('history', 'items', table, name + '.pkl'))
        
        return df.loc[:self.date.strftime("%Y-%m-%d")].iloc[-amount:]

    def talib(self, func_name, amount=0, **args):
        
        func = getattr(abstract, func_name)

        isSeries = True if len(func.output_names) == 1 else False
        names = func.output_names
        if isSeries:
            dic = {}
        else:
            dics = {n:{} for n in names}

        close = self.get('收盤價', amount)
        open_ = self.get('開盤價', amount)
        high  = self.get('最高價', amount)
        low   = self.get('最低價', amount)
        volume= self.get('成交股數', amount)

        for key in close.columns:
            try:
                s = func({'open':open_[key].ffill(),
                               'high':high[key].ffill(),
                               'low':low[key].ffill(),
                               'close':close[key].ffill(),
                               'volume':volume[key].ffill()}, **args)
            except Exception as e:
                if "inputs are all NaN" != str(e):
                    print('Warrning occur during calculating stock '+key+':',e)
                    print('The indicator values are set to NaN.')
                if isSeries:
                    s = pd.Series(index=close[key].index)
                else:
                    s = pd.DataFrame(index=close[key].index, columns=dics.keys())

            if isSeries:
                dic[key] = s
            else:
                for colname, si in zip(names, s):
                    dics[colname][key] = si

        if isSeries:
            ret = pd.DataFrame(dic, index=close.index)
            ret = ret.apply(lambda s:pd.to_numeric(s, errors='coerce'))
        else:
            newdic = {}
            for key, dic in dics.items():
                newdic[key] = pd.DataFrame(dic, close.index).loc[:self.date]
            ret = [newdic[n] for n in names]#pd.Panel(newdic)
            ret = [d.apply(lambda s:pd.to_numeric(s, errors='coerce')) for d in ret]
            
        
        return ret
    
    def get_adj(self, name):
        
        def adj_holiday(item, df):
            all_index = (df.index | item.index).sort_values()
            all_index = all_index[all_index >= item.index[0]]

            df = df.reindex(all_index)
            group = all_index.isin(item.index).cumsum()
            df = df.groupby(group).mean()
            df.index = item.index
            return df
        
        item = self.get(name)
        ratio1 = adj_holiday(item, self.get('otc_cap_divide_ratio'))
        ratio2 = adj_holiday(item, self.get('twse_cap_divide_ratio'))
        ratio3 = adj_holiday(item, self.get('otc_divide_ratio'))
        ratio4 = adj_holiday(item, self.get('twse_divide_ratio'))

        divide_ratio = ( ratio1.reindex_like(item).fillna(1)
         *ratio2.reindex_like(item).fillna(1)
         *ratio3.reindex_like(item).fillna(1)
         *ratio4.reindex_like(item).fillna(1)).cumprod()
        
        divide_ratio[np.isinf(divide_ratio)] = 1
        return item * divide_ratio

