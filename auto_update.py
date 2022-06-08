# coding=utf-8
from finlab.crawler import table_date_range, update_table, to_pickle, out
from finlab.crawler import (
    crawl_price,
    crawl_bargin,
    crawl_pe,
    crawl_monthly_report,
    crawl_finance_statement_by_date,
    crawl_benchmark,
    crawl_twse_divide_ratio,
    crawl_otc_divide_ratio,
    crawl_twse_cap_reduction,
    crawl_otc_cap_reduction,


    date_range,
    month_range,
    season_range,

    widget, out,
    commit,
)


import datetime

from inspect import signature

def auto_update(table_name, crawl_function, time_range=None):

    sig = signature(crawl_function)

    if len(sig.parameters) != 0:
        first_date, last_date = table_date_range(table_name)
        dates = time_range(last_date, datetime.datetime.now())
        if dates:
            update_table(table_name, crawl_function, dates)
    else:
        df = crawl_function()
        to_pickle(df, table_name)


auto_update('price', crawl_price, date_range)
auto_update('bargin_report', crawl_bargin, date_range)
auto_update('pe', crawl_pe, date_range)
auto_update('benchmark', crawl_benchmark, date_range)
auto_update('monthly_report', crawl_monthly_report, month_range)
auto_update('twse_divide_ratio', crawl_twse_divide_ratio)
auto_update('otc_divide_ratio', crawl_otc_divide_ratio)
auto_update('twse_cap_reduction', crawl_twse_cap_reduction)
auto_update('otc_cap_reduction', crawl_otc_cap_reduction)
commit()
