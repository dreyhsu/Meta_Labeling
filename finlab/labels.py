# -*- coding: utf-8 -*-
import numpy as np
import math
import pandas as pd


def trade_point_dicision(b, th=200):
    th = abs(th)
    q = [(b.index[0], b.index[-1])]
    ret = pd.Series(0, b.index)

    while q:
        
        ts, te = q[-1]
        q = q[:-1]
        
        if ts == te:
            continue
        
        bb = b.loc[ts:te]
        delta = (b.loc[te] - b.loc[ts]) / len(bb)
        
        slop = pd.Series(delta, index=bb.index).cumsum() + b.loc[ts]
        diff = bb - slop
        
        tmin,tmax = diff.idxmin(), diff.idxmax()
        dmin,dmax = diff.loc[tmin], diff.loc[tmax]
        
        ps = set([ts, te])
        if dmin < -th:
            ps.add(tmin)
            ret.loc[tmin] = 1
            
        if dmax > th:
            ps.add(tmax)
            ret.loc[tmax] = -1
            
        ps = sorted(list(ps))
        
        for p1, p2 in zip(ps, ps[1:]):
            
            if p1 == ts and p2 == te:
                continue
                
            q.append((p1, p2))
    
    ret.name = 'trade_point_decision'
    return ret

def continuous_trading_signal(s, n):
    
    
    def generate_signal(s):
        if s[0] < s[-1]:
            smin = s.min()
            smax = s.max()
            return (s[-1] - smin) / (smax - smin) / 2 + 0.5
        else:
            smin = s.min()
            smax = s.max()
            return (s[-1] - smin) / (smax - smin) / 2
            
    
    ret = s.rolling(n).apply(generate_signal, raw=True)
    ret.name = 'continuous_trading_signal'
    return ret


def triple_barrier(price, ub, lb, max_period):

    def end_price(s):
        return np.append(s[(s / s[0] > ub) | (s / s[0] < lb)], s[-1])[0]/s[0]
    
    r = np.array(range(max_period))
    
    def end_time(s):
        return np.append(r[(s / s[0] > ub) | (s / s[0] < lb)], max_period-1)[0]

    p = price.rolling(max_period).apply(end_price, raw=True).shift(-max_period+1)
    t = price.rolling(max_period).apply(end_time, raw=True).shift(-max_period+1)
    t = pd.Series([t.index[int(k+i)] if not math.isnan(k+i) else np.datetime64('NaT') 
                   for i, k in enumerate(t)], index=t.index).dropna()
    
    ret = pd.DataFrame({'triple_barrier_profit':p, 'triple_barrier_sell_time':t, 'triple_barrier_signal':0})
    ret.triple_barrier_signal.loc[ret['triple_barrier_profit'] > ub] = 1
    ret.triple_barrier_signal.loc[ret['triple_barrier_profit'] < lb] = -1
    return ret


def fixed_time_horizon(s, n):
    
    std = s.rolling(n*4).std()
    mean = s.rolling(n*4).mean()
    
    ub = (mean + 1.5*std)
    lb = (mean - 1.5*std)
    
    
    ret = pd.Series(0, index=s.index)
    ret[s > ub.shift(-n)] = -1
    ret[s < lb.shift(-n)] = 1
    
    ret.name = 'fixed_time_horizon_' + str(n)
    
    return ret