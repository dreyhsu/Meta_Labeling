# -*- coding: utf-8 -*-
from sklearn.preprocessing import StandardScaler
import keras
from finlab.data import Data
import talib
import numpy as np
import pandas as pd
import talib
import numpy as np
import pandas as pd
import tqdm

def get_price(name="發行量加權股價指數", freq="15T"):
    data = Data()
    twii = data.get(name)
    twii = twii['台股指數']
    twii = twii.resample(freq).first().dropna()
    return twii

def create_features(twii):
    

    sma = talib.SMA(twii, timeperiod=120)
    wma = talib.WMA(twii, timeperiod=120)
    mom = talib.MOM(twii, timeperiod=120)
    k, d = talib.STOCH  (twii, twii, twii, fastk_period=120, slowk_period=60, slowd_period=60)
    k2, d2 = talib.STOCH(twii, twii, twii, fastk_period=240, slowk_period=120, slowd_period=120)
    k3, d3 = talib.STOCH(twii, twii, twii, fastk_period=360, slowk_period=180, slowd_period=180)
    k4, d4 = talib.STOCH(twii, twii, twii, fastk_period=480, slowk_period=240, slowd_period=240)
    k5, d5 = talib.STOCH(twii, twii, twii, fastk_period=640, slowk_period=320, slowd_period=320)
    k6, d6 = talib.STOCH(twii, twii, twii, fastk_period=720, slowk_period=360, slowd_period=360)
    k7, d7 = talib.STOCH(twii, twii, twii, fastk_period=840, slowk_period=420, slowd_period=420)
    k8, d8 = talib.STOCH(twii, twii, twii, fastk_period=960, slowk_period=480, slowd_period=480)

    rsi = talib.RSI (twii, timeperiod=120)
    rsi2 = talib.RSI(twii, timeperiod=240)
    rsi3 = talib.RSI(twii, timeperiod=480)
    rsi4 = talib.RSI(twii, timeperiod=640)
    rsi5 = talib.RSI(twii, timeperiod=720)
    rsi6 = talib.RSI(twii, timeperiod=840)

    macd1, macd2, macd3 = talib.MACD(twii, fastperiod=120, slowperiod=60, signalperiod=60)
    willr = talib.WILLR(twii, twii, twii, timeperiod=120)
    cci = talib.CCI(twii, twii, twii, timeperiod=120)

    return pd.DataFrame({
        'RSIb': rsi / 50,
        'RSIb2': rsi2 / 50,
        'RSIb3': rsi3 / 50,
        'RSIb4': rsi4 / 50,
        'RSIb5': rsi5 / 50,
        'RSIb6': rsi6 / 50,
        'MOMb': mom - 0,
        'KDb': k - d,
        'KDb2': k2 - d2,
        'KDb3': k3 - d3,
        'KDb4': k4 - d4,
        'KDb5': k5 - d5,
        'KDb6': k6 - d6,
        'KDb7': k7 - d7,
        'KDb8': k8 - d8,

        'a5':   (twii.rolling(5).mean()   / twii),
        'a10':  (twii.rolling(10).mean()  / twii),
        'a20':  (twii.rolling(20).mean()  / twii),
        'a40':  (twii.rolling(40).mean()  / twii),
        'a80':  (twii.rolling(80).mean()  / twii),
        'a160': (twii.rolling(160).mean() / twii),
        'a320': (twii.rolling(320).mean() / twii),
        'a640': (twii.rolling(640).mean() / twii),
        'a720': (twii.rolling(720).mean() / twii),
        'a840': (twii.rolling(840).mean() / twii),
        'a960': (twii.rolling(960).mean() / twii),
        'a1024':(twii.rolling(1024).mean() / twii),
        'b1': twii/twii.shift(50),
        'b2': twii/twii.shift(100),
        'b3': twii/twii.shift(150),
        'b4': twii/twii.shift(200),
        'b5': twii/twii.shift(250),
        'b6': twii/twii.shift(300),
        'b7': twii/twii.shift(350),
        'LINEARREG_SLOPE0': talib.LINEARREG_SLOPE(twii, 60),
        'LINEARREG_SLOPE1': talib.LINEARREG_SLOPE(twii, 120),

        'ADXR0': talib.ADXR(twii, twii, twii, 60),
        'ADXR1': talib.ADXR(twii, twii, twii, 120),
        'ADXR2': talib.ADXR(twii, twii, twii, 240),
        'ADXR3': talib.ADXR(twii, twii, twii, 360),
        'ADXR4': talib.ADXR(twii, twii, twii, 480),
        'ADXR5': talib.ADXR(twii, twii, twii, 640),
    })

def scale(dataset):
    ss = StandardScaler()
    dataset_scaled = ss.fit_transform(dataset)
    return ss, pd.DataFrame(dataset_scaled, columns=dataset.columns, index=dataset.index)

def dropna(x, y):
    isna = (x.isnull().sum(axis=1) != 0) | y.isnull()
    return x[~isna], y[~isna]



def neural_network_classifier_fit(x, y):

    model = keras.models.Sequential()
    model.add(keras.layers.Dense(100, activation="relu", input_shape=(x.shape[1],)))
    model.add(keras.layers.Dense(1, activation="sigmoid"))
    model.compile(optimizer="adam", loss="binary_crossentropy", metrics=['accuracy'])

    model.summary()
    
    get_best_model = keras.callbacks.ModelCheckpoint('nn.mdl', monitor='loss')
    model.fit(x, y, 
              batch_size=5000, epochs=200, validation_split=0.2, callbacks=[get_best_model])
    
    return model

def calculate_3d_feature(x, y_, n=42):

    assert len(x) == len(y_)
    
    X = []
    y = []
    indexes = []

    for i in tqdm.tqdm_notebook(range(0, len(x)-n)):
        X.append(x.iloc[i:i+n].values)
        y.append(y_.iloc[i+n-1])
        indexes.append(x.index[i+n-1])

    X = np.array(X)
    y = np.array(y)
    indexes = np.array(indexes)
    return X, y, indexes


def cnn_classifier_fit(x, y):
    
    x, y, index = calculate_3d_feature(x, y)
    
    import keras
    model = keras.Sequential()

    model.add(keras.layers.Conv1D(filters=15, kernel_size=15, activation='relu', input_shape=x[0].shape))
    model.add(keras.layers.Conv1D(filters=15, kernel_size=15, activation='relu'))
    model.add(keras.layers.Flatten())
    model.add(keras.layers.Dense(units=120, activation='relu'))
    model.add(keras.layers.Dropout(0.3))
    model.add(keras.layers.Dense(units=84, activation='relu'))
    model.add(keras.layers.Dropout(0.3))
    model.add(keras.layers.Dense(units=1, ))

    adam = keras.optimizers.Adam(lr=0.001, beta_1=0.9, beta_2=0.99, epsilon=None, decay=0.01, amsgrad=False)

    model.compile(loss='mse',
                    optimizer=adam)

    print(model.summary())

    history = model.fit(x, y,
                        batch_size=10000,
                        epochs=100,
                        verbose=1,
                        validation_split=0.1, )
    return model

def lstm_classifier_fit(x, y):
    
    x, y, index = calculate_3d_feature(x, y)
    
    model = keras.models.Sequential()
    
    model.add(keras.layers.LSTM(100, return_sequences=True, input_shape=x[0].shape))
    model.add(keras.layers.LSTM(100))
    model.add(keras.layers.Dense(8))
    model.add(keras.layers.Dense(1,kernel_initializer="uniform",activation='linear'))

    adam = keras.optimizers.Adam(0.0006)

    model.compile(optimizer=adam, loss="binary_crossentropy", metrics=['accuracy'])

    get_best_model = keras.callbacks.ModelCheckpoint("lstm.mdl", monitor="val_acc")

    history = model.fit(
        x,  
        y, 
        batch_size=5000, 
        epochs=300, 
        validation_split=0.2, 
        callbacks=[get_best_model])

    return model

def predict_3d_feature(model, x):
    
    x, y, index = calculate_3d_feature(x, x.iloc[:,0], n=model.input_shape[-1])
    y = model.predict(x)
    return pd.Series(y.reshape(1, len(y))[0], index)

def predict_feature(model, x):
    y = model.predict(x)
    return pd.Series(y.reshape(1, len(y))[0], x.index)

def check_stationary(s):

    from pandas import Series
    from statsmodels.tsa.stattools import adfuller
    from numpy import log
    X = s.dropna()[::int(len(s)/10000)]
    result = adfuller(X)
    return result[1]

def backtest(signal, returns, stop_profit=100, stop_loss=-100):
    
    ret = {}
    hold = False
    holdt = 0
    p = 0
    
    
    for r, s, d in zip(returns, signal, signal.index):
        
        if hold:
            p += r
            holdt += 1
            
            if p > stop_profit or p < stop_loss or holdt > 10:
                hold = False
                ret[d] = p
                p = 0
                holdt = 0
        
        if s:
            hold = True

    return ret


def fugle_realtime(api_token, twii, model, ss, freq="15T", lookback=10000):
    
    from fugle_realtime import intraday
    if twii.index.tzinfo is None:
        twii.index = twii.index.tz_localize("Asia/Taipei")
    
    df = intraday.chart(apiToken=api_token, output="dataframe", symbolId="TWSE_SEM_INDEX_1")
    df.index = df['at']
    df.index = df.index.tz_convert("Asia/Taipei")
    df = df.resample(freq).first()

    twii_temp = twii.append(df.close).iloc[-lookback:]
    features = create_features(twii_temp).dropna()
    
    if len(features) == 0:
        print("fail! please increase lookback period")
        
    y = model.predict(ss.transform(features))
    return pd.DataFrame({'twii':twii_temp.loc[features.index].values, 
                         'model': y.reshape(1, len(y))[0]})