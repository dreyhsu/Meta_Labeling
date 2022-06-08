import pandas as pd

def main():
    # long candidate
    raw_df = pd.read_csv(r'C:\Users\Drey\finlab_ml_course\training_data\bband_long.csv')
    df = raw_df[(raw_df.mrl_m_result > .9) & (raw_df.side == 1)].sort_values(by=['accu'], ascending=False)
    df.to_csv('result/result_long_mrl.csv', index=False)
    df = raw_df[(raw_df.tl_m_result > .8) & (raw_df.side == 2)].sort_values(by=['accu'], ascending=False)
    df.to_csv('result/result_long_trend.csv', index=False)
    # short candidate
    # raw_df = pd.read_csv(r'C:\Users\Drey\finlab_ml_course\training_data\bband_short.csv')
    # df = raw_df[(raw_df.side_m1_result == -1) & (raw_df.side == 1)].sort_values(by=['accu'])
    # df.to_csv('result/result_short.csv', index=False)


if __name__ == '__main__':
    main()