import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
from talib.abstract import *
from sklearn.preprocessing import MinMaxScaler
import joblib
from argparse import ArgumentParser
parser = ArgumentParser()
parser.add_argument("--ls", help="long_short", type=str)
parser.add_argument("--date", help="date", type=str)
args = parser.parse_args()

from finlab.data import Data

database = Data()
close = database.get("收盤價")
open_ = database.get("開盤價")
high = database.get("最高價")
low = database.get("最低價")
vol = database.get("成交股數")
accu = database.get("成交金額")
rev = database.get("當月營收")
com_rev = database.get("上月比較增減(%)")
d_yield = database.get("殖利率(%)")
pb = database.get("股價淨值比")

start_date = '2021-01-01'
close = close[close.index > start_date]
open_ = open_[open_.index > start_date]
high = high[high.index > start_date]
low = low[low.index > start_date]
vol = vol[vol.index > start_date]
accu = accu[accu.index > start_date]
rev = rev[rev.index > start_date]
com_rev = com_rev[com_rev.index > start_date]
d_yield = d_yield[d_yield.index > start_date]
pb = pb[pb.index > start_date]

def MA(close, n):
    return close.rolling(window=n).mean()

def bias(close, n):
    return close / close.rolling(n, min_periods=1).mean()

def acc(close, n):
    return close.shift(n) / (close.shift(2*n) + close) * 2

def mom(rev, n):
    return (rev / rev.shift(1)).shift(n)

# vol = vol.reset_index()
sid = '0050'
benchmark = pd.DataFrame({'close': close[sid], 'high': high[sid], 'low': low[sid], 'volume': vol[sid]})

benchmark['b_OBV'] = OBV(benchmark.close, benchmark.volume)
benchmark['b_AD'] = AD(benchmark.high, benchmark.low, benchmark.close, benchmark.volume)
benchmark['b_ADOSC'] = ADOSC(benchmark.high, benchmark.low, benchmark.close, benchmark.volume, fastperiod=3, slowperiod=10)

benchmark['b_MA5'] = MA(benchmark['close'], 5) - benchmark['close']
benchmark['b_MA20'] = MA(benchmark['close'], 20) - benchmark['close']
benchmark['b_MA60'] = MA(benchmark['close'], 60) - benchmark['close']

benchmark['b_bias5'] = bias(benchmark['close'], 5)
benchmark['b_bias10'] = bias(benchmark['close'], 10)
benchmark['b_bias20'] = bias(benchmark['close'], 20)
benchmark['b_bias60'] = bias(benchmark['close'], 60)

benchmark['b_acc5'] = acc(benchmark['close'], 5)
benchmark['b_acc10'] = acc(benchmark['close'], 10)
benchmark['b_acc20'] = acc(benchmark['close'], 20)
benchmark['b_acc60'] = acc(benchmark['close'], 60)

window_stdev = 50
benchmark['b_log_ret'] = np.log(benchmark['close']).diff()
benchmark['b_volatility'] = benchmark['b_log_ret'].rolling(window=window_stdev, min_periods=window_stdev, center=False).std()

def main(date, sid, close, open_, high , low, vol, rev, com_rev, d_yield, pb, benchmark):
    t_final = 5
    def get_Daily_Volatility(close,span0=20):
        # simple percentage returns
        df0=close.pct_change()
        # 20 days, a month EWM's std as boundary
        df0=df0.ewm(span=span0).std()
        df0.dropna(inplace=True)
        return df0

    def get_3_barriers():
        #create a container
        barriers = pd.DataFrame(columns=['days_passed', 
                'price', 'vert_barrier', \
                'top_barrier', 'bottom_barrier', 'long_ret', 'short_ret'], \
                index = daily_volatility.index)
        for day, vol in daily_volatility.iteritems():
            days_passed = len(daily_volatility.loc \
                        [daily_volatility.index[0] : day])
            #set the vertical barrier 
            if (days_passed + t_final < len(daily_volatility.index) \
                and t_final != 0):
                vert_barrier = daily_volatility.index[
                                    days_passed + t_final]
            else:
                vert_barrier = np.nan
            #set the top barrier
            if upper_lower_multipliers[0] > 0:
                top_barrier = prices.loc[day] + prices.loc[day] * \
                            upper_lower_multipliers[0] * vol
            else:
                #set it to NaNs
                top_barrier = pd.Series(index=prices.index)
            #set the bottom barrier
            if upper_lower_multipliers[1] > 0:
                bottom_barrier = prices.loc[day] - prices.loc[day] * \
                            upper_lower_multipliers[1] * vol
            else: 
                #set it to NaNs
                bottom_barrier = pd.Series(index=prices.index)

            barriers.loc[day, ['days_passed', 'price', 'vert_barrier','top_barrier', 'bottom_barrier']] = \
            days_passed, prices.loc[day], vert_barrier, \
            top_barrier, bottom_barrier
        return barriers

    data = pd.DataFrame({'close': close[sid],
                        'open': open_[sid],
                        'high': high[sid],
                        'low': low[sid],
                        'volume': vol[sid],
                        'accu': accu[sid]})

    data = data.reset_index()
    data.dropna(axis=0, how='any', inplace=True)
    rev = rev.reset_index()
    # print(f'shape of df {data.shape}')
    data = pd.merge(data,rev[['date',sid]], on="date", how='outer')
    # print(f'shape of df {data.shape}')
    data = data.sort_values(by=['date'])
    data = data.rename(columns={sid: "rev"})
    data['rev'].fillna(method='ffill', inplace=True)

    com_rev = com_rev.reset_index()
    # print(f'shape of df {data.shape}')
    data = pd.merge(data,com_rev[['date',sid]], on="date", how='outer')
    # print(f'shape of df {data.shape}')
    data = data.sort_values(by=['date'])
    data = data.rename(columns={sid: "com_rev"})
    data['com_rev'].fillna(method='ffill', inplace=True)

    d_yield = d_yield.reset_index()
    # print(f'shape of df {data.shape}')
    data = pd.merge(data,d_yield[['date',sid]], on="date", how='outer')
    # print(f'shape of df {data.shape}')
    data = data.rename(columns={sid: "d_yield"})
    data['d_yield'].fillna(method='ffill', inplace=True)

    pb = pb.reset_index()
    # print(f'shape of df {data.shape}')
    data = pd.merge(data,pb[['date',sid]], on="date", how='outer')
    # print(f'shape of df {data.shape}')
    data = data.rename(columns={sid: "pb"})
    data['pb'].fillna(method='ffill', inplace=True)

    benchmark = benchmark.reset_index()
    benchmark_list = ['date', 'b_OBV', 'b_AD', 'b_ADOSC', 'b_MA5', 'b_MA20', 'b_MA60', 'b_bias5', 'b_bias10', 'b_bias20', 'b_bias60'
    , 'b_acc5', 'b_acc10', 'b_acc20', 'b_acc60', 'b_volatility']
    data = pd.merge(data,benchmark[benchmark_list], on="date", how='outer')
    for features in benchmark_list:
        data[features].fillna(method='ffill', inplace=True)

    data = data.set_index('date')
    # print(f'shape of df {data.shape}')
    data.dropna(axis=0, how='any', inplace=True)
    # print(f'shape of df {data.shape}')
    # data.tail()

    # talib
    # data.to_csv('test.csv', index=False)
    data['upperband'], data['middleband'], data['lowerband'] = BBANDS(data.close, 20, 2., 2. ,0)
    data['OBV'] = OBV(data.close, data.volume)
    data['AD'] = AD(data.high, data.low, data.close, data.volume)
    data['ADOSC'] = ADOSC(data.high, data.low, data.close, data.volume, fastperiod=3, slowperiod=10)
    data['K'], data['D'] = STOCH(data.high, data.low, data.close, fastk_period=9, slowk_period=3,slowd_period=3)

    data['MA5'] = MA(data['close'], 5) - data['close']
    data['MA20'] = MA(data['close'], 20) - data['close']
    data['MA60'] = MA(data['close'], 60) - data['close']
    data['_MA20'] = MA(data['close'], 20)

    data['bias5'] = bias(data['close'], 5)
    data['bias10'] = bias(data['close'], 10)
    data['bias20'] = bias(data['close'], 20)
    data['bias60'] = bias(data['close'], 60)

    data['acc5'] = acc(data['close'], 5)
    data['acc10'] = acc(data['close'], 10)
    data['acc20'] = acc(data['close'], 20)
    data['acc60'] = acc(data['close'], 60)

    data['rsi'] = RSI(data['close'], window=14)
    data['MACD'], data['signal'], data['hist'] = MACD(data['close'], fastperiod=12,  slowperiod=26,  signalperiod=9)
    # Compute sides
    data['side'] = np.nan
    data['high1'] = data['high'].shift(1)
    data['low1'] = data['low'].shift(1)
    data['close1'] = data['close'].shift(1)

    con1 = (data['close'] >= data['lowerband']) & (data['low1'] <= data['lowerband']) & (data['close'] > data['close1'])
    con2 = (data['high'] >= data['upperband']) & (data['high1'] >= data['upperband']) & (data['close'] > data['close1'])

    data.loc[con1, 'side'] = 1
    data.loc[con2, 'side'] = 2

    data['side'].fillna(value=0, inplace=True)
    # raw_data = data.copy()

    # Log Returns
    data['log_ret'] = np.log(data['close']).diff()
    # Momentum
    data['mom1'] = data['close'].pct_change(periods=1)
    data['mom2'] = data['close'].pct_change(periods=2)
    data['mom3'] = data['close'].pct_change(periods=3)
    data['mom4'] = data['close'].pct_change(periods=4)
    data['mom5'] = data['close'].pct_change(periods=5)

    # Volatility
    window_stdev = 50
    data['volatility'] = data['log_ret'].rolling(window=window_stdev, min_periods=window_stdev, center=False).std()

    # Serial Correlation (Takes about 4 minutes)
    window_autocorr = 50

    data['autocorr_1'] = data['log_ret'].rolling(window=window_autocorr, min_periods=window_autocorr, center=False).apply(lambda x: x.autocorr(lag=1), raw=False)
    data['autocorr_2'] = data['log_ret'].rolling(window=window_autocorr, min_periods=window_autocorr, center=False).apply(lambda x: x.autocorr(lag=2), raw=False)
    data['autocorr_3'] = data['log_ret'].rolling(window=window_autocorr, min_periods=window_autocorr, center=False).apply(lambda x: x.autocorr(lag=3), raw=False)
    data['autocorr_4'] = data['log_ret'].rolling(window=window_autocorr, min_periods=window_autocorr, center=False).apply(lambda x: x.autocorr(lag=4), raw=False)
    data['autocorr_5'] = data['log_ret'].rolling(window=window_autocorr, min_periods=window_autocorr, center=False).apply(lambda x: x.autocorr(lag=5), raw=False)

    # Get the various log -t returns
    data['log_t1'] = data['log_ret'].shift(1)
    data['log_t2'] = data['log_ret'].shift(2)
    data['log_t3'] = data['log_ret'].shift(3)
    data['log_t4'] = data['log_ret'].shift(4)
    data['log_t5'] = data['log_ret'].shift(5)

    # Add fast and slow moving averages
    fast_window = 7
    slow_window = 15

    data['fast_mavg'] = data['close'].rolling(window=fast_window, min_periods=fast_window, center=False).mean()
    data['slow_mavg'] = data['close'].rolling(window=slow_window, min_periods=slow_window, center=False).mean()

    data['sma'] = np.nan

    long_signals = data['fast_mavg'] >= data['slow_mavg']
    short_signals = data['fast_mavg'] < data['slow_mavg']
    data.loc[long_signals, 'sma'] = 1
    data.loc[short_signals, 'sma'] = -1
    data['sma'].fillna(value=0, inplace=True)

    price = data['close']
    daily_volatility = get_Daily_Volatility(price)
    data['daily_volatility'] = daily_volatility
    # how many days we hold the stock which set the vertical barrier
    t_final = 10 
    #the up and low boundary multipliers
    if args.ls == 'long':
        upper_lower_multipliers = [3, 1]
    else:
        upper_lower_multipliers = [1, 3]
    prices = price[daily_volatility.index]
    barriers = get_3_barriers()
    barriers['out'] = None
    data = data.reset_index()
    barriers = barriers.reset_index()
    data = pd.merge(data,barriers[['date','top_barrier', 'bottom_barrier']], on="date")
    data.dropna(axis=0, how='any', inplace=True)
    data = data.reset_index()

    # normalize
    feature_list = ['com_rev', 'd_yield', 'pb', 'AD', 'OBV', 'ADOSC', 'bias5',
       'bias10', 'bias20', 'bias60', 'acc5', 'acc10', 'acc20', 'acc60', 'rsi',
       'log_ret', 'mom1', 'mom2', 'mom3', 'mom4', 'mom5', 'volatility',
       'MA5', 'MA20', 'MA60', 'MACD', 'signal', 'hist',
       'autocorr_1', 'autocorr_2', 'autocorr_3', 'autocorr_4', 'autocorr_5',
       'log_t1', 'log_t2', 'log_t3', 'log_t4', 'log_t5', 'b_OBV', 'b_AD', 'b_ADOSC',
       'b_MA5', 'b_MA20', 'b_MA60', 'b_bias5', 'b_bias10', 'b_bias20', 'b_bias60',
       'b_acc5', 'b_acc10', 'b_acc20', 'b_acc60', 'b_volatility']

    scale = MinMaxScaler(feature_range = (-1, 1)) #z-scaler物件
    for item in feature_list:
        data[item] = scale.fit_transform(np.array(data[item].to_list()).reshape(-1, 1))

    mrl_m = joblib.load(r'C:\Users\Drey\finlab_ml_course\lazypredict\mrs_long_LGBM_31_0520.pkl')
    # mrs_m = joblib.load(r'C:\Users\Drey\finlab_ml_course\lazypredict\0501_mrs_short_LGBM.pkl')
    tl_m = joblib.load(r'C:\Users\Drey\finlab_ml_course\lazypredict\trend_long_LGBM_31_0520.pkl')
    # ts_m = joblib.load(r'C:\Users\Drey\finlab_ml_course\lazypredict\0501_trend_short_LGBM.pkl')

    X = data[feature_list]
    # model_dict = {'mrl_m':mrl_m, 'mrs_m':mrs_m, 'tl_m':tl_m, 'ts_m':ts_m}
    # model_dict = {'mrl_m':mrl_m, 'tl_m':tl_m}
    model_dict = {'mrl_m_result':mrl_m, 'tl_m_result':tl_m}
    for key in model_dict:
        # make predictions for test data
        y_pred = model_dict[key].predict_proba(X)[:, 1]
        data[key] = y_pred

    # data['side_1_result'] = [1 if (x > 0) & (y == 0) else 0 for x,y in zip(data['tl_m'], data['mrs_m'])]
    # data['side_m1_result'] = [-1 if (x > 0) & (y == 0) else 0 for x,y in zip(data['ts_m'], data['mrl_m'])]
    # data['mrl_m_result'] = [x if (x > 0.9) else 0 for x in data['mrl_m']]
    # data['tl_m_result'] = [x if (x > 0.9) else 0 for x in data['tl_m']]
    data = data.set_index('date')
    # data.to_csv('test.csv')
    result_df = data[['close', 'accu' ,'top_barrier', 'bottom_barrier', 'side', 'mrl_m_result', 'tl_m_result']].loc[date]
    # result_df = data.copy()
    result_df['sid'] = sid
    result_df = result_df.to_frame().T
    return result_df

if __name__ == '__main__':
    sid_list = pd.read_csv('sid.csv')
    tar_list = list(sid_list['sid'].unique())
    date = args.date
    for i, item in enumerate(tqdm(tar_list)):
        sid = str(item)
        if i == 0:
            X = main(date, sid, close, open_, high , low, vol, rev, com_rev, d_yield, pb, benchmark)
        else:
            try:
                X = pd.concat([X, main(date, sid, close, open_, high , low, vol, rev, com_rev, d_yield, pb, benchmark)])
            except KeyError:
                continue
            except:
                continue
    if args.ls == 'long':
        X.to_csv('training_data/bband_long.csv', index=False)
    else:
        X.to_csv('training_data/bband_short.csv', index=False)