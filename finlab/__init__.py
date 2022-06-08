# -*- coding: utf-8 -*-
import pandas as pd
from .data import Data

def talib_all_stock(ndays, func, **args):

    isSeries = True if len(func.output_names) == 1 else False
    names = func.output_names
    if isSeries:
        dic = {}
    else:
        dics = {n:{} for n in names}
    
    data = Data()
    close = data.get('收盤價', 1000000)
    open_ = data.get('開盤價', 1000000)
    high = data.get('最高價', 1000000)
    low = data.get('最低價', 1000000)
    volume = data.get('成交股數', 1000000)/1000

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
    else:
        newdic = {}
        for key, dic in dics.items():
            newdic[key] = pd.DataFrame(dic, close.index)
        ret = [newdic[n] for n in names]#pd.Panel(newdic)
    return ret


