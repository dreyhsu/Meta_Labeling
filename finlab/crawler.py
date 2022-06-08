# -*- coding: utf-8 -*-
import datetime
import requests
import pandas as pd
import pickle
import time
import urllib
import os
from io import StringIO
import numpy as np
import warnings
import os
import datetime
import time
from tqdm import tnrange, tqdm_notebook
from requests.exceptions import ConnectionError
from requests.exceptions import ReadTimeout
import ipywidgets as widgets
import pip
import pandas



def import_or_install(package):
    try:
        __import__(package)
    except ImportError:
        print('Please install lxml(pip install lxml)')
        
    # try:
    #     versions = [int(i) for i in pandas.__version__.split('.')]
    #     assert (versions[0] == 1) & (versions[1] >= 1) & (versions[2] >= 4)
    # except:
    #     v = pandas.__version__
    #     raise Exception(f'Your pandas version is {v}. Please install pandas >= 1.1.4.')

import_or_install("lxml")


import random
import copy
def generate_random_header():
    random_user_agents = {'chrome': ['Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
      'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36',
      'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36',
      'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36',
      'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2226.0 Safari/537.36',
      'Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36',
      'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36',
      'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36',
      'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36',
      'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36',
      'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36',
      'Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36',
      'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36',
      'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36',
      'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
      'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1944.0 Safari/537.36',
      'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.3319.102 Safari/537.36',
      'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2309.372 Safari/537.36',
      'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2117.157 Safari/537.36',
      'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36',
      'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1866.237 Safari/537.36',
      'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/4E423F',
      'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.116 Safari/537.36 Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10',
      'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.517 Safari/537.36',
      'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36',
      'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1664.3 Safari/537.36',
      'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1664.3 Safari/537.36',
      'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.16 Safari/537.36',
      'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1623.0 Safari/537.36',
      'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.17 Safari/537.36',
      'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.62 Safari/537.36',
      'Mozilla/5.0 (X11; CrOS i686 4319.74.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.57 Safari/537.36',
      'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.2 Safari/537.36',
      'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1468.0 Safari/537.36',
      'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1467.0 Safari/537.36',
      'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1464.0 Safari/537.36',
      'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1500.55 Safari/537.36',
      'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36',
      'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36',
      'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36',
      'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36',
      'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36',
      'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36',
      'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.90 Safari/537.36',
      'Mozilla/5.0 (X11; NetBSD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36',
      'Mozilla/5.0 (X11; CrOS i686 3912.101.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36',
      'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.60 Safari/537.17',
      'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1309.0 Safari/537.17',
      'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.15 (KHTML, like Gecko) Chrome/24.0.1295.0 Safari/537.15',
      'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.14 (KHTML, like Gecko) Chrome/24.0.1292.0 Safari/537.14'],
     'opera': ['Opera/9.80 (X11; Linux i686; Ubuntu/14.10) Presto/2.12.388 Version/12.16',
      'Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14',
      'Mozilla/5.0 (Windows NT 6.0; rv:2.0) Gecko/20100101 Firefox/4.0 Opera 12.14',
      'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14',
      'Opera/12.80 (Windows NT 5.1; U; en) Presto/2.10.289 Version/12.02',
      'Opera/9.80 (Windows NT 6.1; U; es-ES) Presto/2.9.181 Version/12.00',
      'Opera/9.80 (Windows NT 5.1; U; zh-sg) Presto/2.9.181 Version/12.00',
      'Opera/12.0(Windows NT 5.2;U;en)Presto/22.9.168 Version/12.00',
      'Opera/12.0(Windows NT 5.1;U;en)Presto/22.9.168 Version/12.00',
      'Mozilla/5.0 (Windows NT 5.1) Gecko/20100101 Firefox/14.0 Opera/12.0',
      'Opera/9.80 (Windows NT 6.1; WOW64; U; pt) Presto/2.10.229 Version/11.62',
      'Opera/9.80 (Windows NT 6.0; U; pl) Presto/2.10.229 Version/11.62',
      'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52',
      'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; de) Presto/2.9.168 Version/11.52',
      'Opera/9.80 (Windows NT 5.1; U; en) Presto/2.9.168 Version/11.51',
      'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; de) Opera 11.51',
      'Opera/9.80 (X11; Linux x86_64; U; fr) Presto/2.9.168 Version/11.50',
      'Opera/9.80 (X11; Linux i686; U; hu) Presto/2.9.168 Version/11.50',
      'Opera/9.80 (X11; Linux i686; U; ru) Presto/2.8.131 Version/11.11',
      'Opera/9.80 (X11; Linux i686; U; es-ES) Presto/2.8.131 Version/11.11',
      'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/5.0 Opera 11.11',
      'Opera/9.80 (X11; Linux x86_64; U; bg) Presto/2.8.131 Version/11.10',
      'Opera/9.80 (Windows NT 6.0; U; en) Presto/2.8.99 Version/11.10',
      'Opera/9.80 (Windows NT 5.1; U; zh-tw) Presto/2.8.131 Version/11.10',
      'Opera/9.80 (Windows NT 6.1; Opera Tablet/15165; U; en) Presto/2.8.149 Version/11.1',
      'Opera/9.80 (X11; Linux x86_64; U; Ubuntu/10.10 (maverick); pl) Presto/2.7.62 Version/11.01',
      'Opera/9.80 (X11; Linux i686; U; ja) Presto/2.7.62 Version/11.01',
      'Opera/9.80 (X11; Linux i686; U; fr) Presto/2.7.62 Version/11.01',
      'Opera/9.80 (Windows NT 6.1; U; zh-tw) Presto/2.7.62 Version/11.01',
      'Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.7.62 Version/11.01',
      'Opera/9.80 (Windows NT 6.1; U; sv) Presto/2.7.62 Version/11.01',
      'Opera/9.80 (Windows NT 6.1; U; en-US) Presto/2.7.62 Version/11.01',
      'Opera/9.80 (Windows NT 6.1; U; cs) Presto/2.7.62 Version/11.01',
      'Opera/9.80 (Windows NT 6.0; U; pl) Presto/2.7.62 Version/11.01',
      'Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.7.62 Version/11.01',
      'Opera/9.80 (Windows NT 5.1; U;) Presto/2.7.62 Version/11.01',
      'Opera/9.80 (Windows NT 5.1; U; cs) Presto/2.7.62 Version/11.01',
      'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.13) Gecko/20101213 Opera/9.80 (Windows NT 6.1; U; zh-tw) Presto/2.7.62 Version/11.01',
      'Mozilla/5.0 (Windows NT 6.1; U; nl; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 Opera 11.01',
      'Mozilla/5.0 (Windows NT 6.1; U; de; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 Opera 11.01',
      'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; de) Opera 11.01',
      'Opera/9.80 (X11; Linux x86_64; U; pl) Presto/2.7.62 Version/11.00',
      'Opera/9.80 (X11; Linux i686; U; it) Presto/2.7.62 Version/11.00',
      'Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.6.37 Version/11.00',
      'Opera/9.80 (Windows NT 6.1; U; pl) Presto/2.7.62 Version/11.00',
      'Opera/9.80 (Windows NT 6.1; U; ko) Presto/2.7.62 Version/11.00',
      'Opera/9.80 (Windows NT 6.1; U; fi) Presto/2.7.62 Version/11.00',
      'Opera/9.80 (Windows NT 6.1; U; en-GB) Presto/2.7.62 Version/11.00',
      'Opera/9.80 (Windows NT 6.1 x64; U; en) Presto/2.7.62 Version/11.00',
      'Opera/9.80 (Windows NT 6.0; U; en) Presto/2.7.39 Version/11.00'],
     'firefox': ['Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1',
      'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0',
      'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0',
      'Mozilla/5.0 (X11; Linux i586; rv:31.0) Gecko/20100101 Firefox/31.0',
      'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0',
      'Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0',
      'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20120101 Firefox/29.0',
      'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:25.0) Gecko/20100101 Firefox/29.0',
      'Mozilla/5.0 (X11; OpenBSD amd64; rv:28.0) Gecko/20100101 Firefox/28.0',
      'Mozilla/5.0 (X11; Linux x86_64; rv:28.0) Gecko/20100101  Firefox/28.0',
      'Mozilla/5.0 (Windows NT 6.1; rv:27.3) Gecko/20130101 Firefox/27.3',
      'Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:27.0) Gecko/20121011 Firefox/27.0',
      'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:25.0) Gecko/20100101 Firefox/25.0',
      'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:25.0) Gecko/20100101 Firefox/25.0',
      'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:24.0) Gecko/20100101 Firefox/24.0',
      'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0',
      'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:24.0) Gecko/20100101 Firefox/24.0',
      'Mozilla/5.0 (Windows NT 6.2; rv:22.0) Gecko/20130405 Firefox/23.0',
      'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20130406 Firefox/23.0',
      'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:23.0) Gecko/20131011 Firefox/23.0',
      'Mozilla/5.0 (Windows NT 6.2; rv:22.0) Gecko/20130405 Firefox/22.0',
      'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:22.0) Gecko/20130328 Firefox/22.0',
      'Mozilla/5.0 (Windows NT 6.1; rv:22.0) Gecko/20130405 Firefox/22.0',
      'Mozilla/5.0 (Microsoft Windows NT 6.2.9200.0); rv:22.0) Gecko/20130405 Firefox/22.0',
      'Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:16.0.1) Gecko/20121011 Firefox/21.0.1',
      'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:16.0.1) Gecko/20121011 Firefox/21.0.1',
      'Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:21.0.0) Gecko/20121011 Firefox/21.0.0',
      'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:21.0) Gecko/20130331 Firefox/21.0',
      'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:21.0) Gecko/20100101 Firefox/21.0',
      'Mozilla/5.0 (X11; Linux i686; rv:21.0) Gecko/20100101 Firefox/21.0',
      'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20130514 Firefox/21.0',
      'Mozilla/5.0 (Windows NT 6.2; rv:21.0) Gecko/20130326 Firefox/21.0',
      'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:21.0) Gecko/20130401 Firefox/21.0',
      'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:21.0) Gecko/20130331 Firefox/21.0',
      'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:21.0) Gecko/20130330 Firefox/21.0',
      'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0',
      'Mozilla/5.0 (Windows NT 6.1; rv:21.0) Gecko/20130401 Firefox/21.0',
      'Mozilla/5.0 (Windows NT 6.1; rv:21.0) Gecko/20130328 Firefox/21.0',
      'Mozilla/5.0 (Windows NT 6.1; rv:21.0) Gecko/20100101 Firefox/21.0',
      'Mozilla/5.0 (Windows NT 5.1; rv:21.0) Gecko/20130401 Firefox/21.0',
      'Mozilla/5.0 (Windows NT 5.1; rv:21.0) Gecko/20130331 Firefox/21.0',
      'Mozilla/5.0 (Windows NT 5.1; rv:21.0) Gecko/20100101 Firefox/21.0',
      'Mozilla/5.0 (Windows NT 5.0; rv:21.0) Gecko/20100101 Firefox/21.0',
      'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:21.0) Gecko/20100101 Firefox/21.0',
      'Mozilla/5.0 (Windows NT 6.2; Win64; x64;) Gecko/20100101 Firefox/20.0',
      'Mozilla/5.0 (Windows x86; rv:19.0) Gecko/20100101 Firefox/19.0',
      'Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/19.0',
      'Mozilla/5.0 (Windows NT 6.1; rv:14.0) Gecko/20100101 Firefox/18.0.1',
      'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:18.0)  Gecko/20100101 Firefox/18.0',
      'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:17.0) Gecko/20100101 Firefox/17.0.6'],
     'internetexplorer': ['Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko',
      'Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; Trident/7.0;  rv:11.0) like Gecko',
      'Mozilla/5.0 (compatible; MSIE 10.6; Windows NT 6.1; Trident/5.0; InfoPath.2; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727) 3gpp-gba UNTRUSTED/1.0',
      'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 7.0; InfoPath.3; .NET CLR 3.1.40767; Trident/6.0; en-IN)',
      'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
      'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
      'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/5.0)',
      'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/4.0; InfoPath.2; SV1; .NET CLR 2.0.50727; WOW64)',
      'Mozilla/5.0 (compatible; MSIE 10.0; Macintosh; Intel Mac OS X 10_7_3; Trident/6.0)',
      'Mozilla/4.0 (Compatible; MSIE 8.0; Windows NT 5.2; Trident/6.0)',
      'Mozilla/4.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/5.0)',
      'Mozilla/1.22 (compatible; MSIE 10.0; Windows 3.1)',
      'Mozilla/5.0 (Windows; U; MSIE 9.0; WIndows NT 9.0; en-US))',
      'Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)',
      'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 7.1; Trident/5.0)',
      'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; Media Center PC 6.0; InfoPath.3; MS-RTC LM 8; Zune 4.7)',
      'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; Media Center PC 6.0; InfoPath.3; MS-RTC LM 8; Zune 4.7',
      'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; Zune 4.0; InfoPath.3; MS-RTC LM 8; .NET4.0C; .NET4.0E)',
      'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; chromeframe/12.0.742.112)',
      'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)',
      'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)',
      'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; Zune 4.0; Tablet PC 2.0; InfoPath.3; .NET4.0C; .NET4.0E)',
      'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0',
      'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; yie8)',
      'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET CLR 1.1.4322; .NET4.0C; Tablet PC 2.0)',
      'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; FunWebProducts)',
      'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; chromeframe/13.0.782.215)',
      'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; chromeframe/11.0.696.57)',
      'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0) chromeframe/10.0.648.205',
      'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/4.0; GTB7.4; InfoPath.1; SV1; .NET CLR 2.8.52393; WOW64; en-US)',
      'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0; chromeframe/11.0.696.57)',
      'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/4.0; GTB7.4; InfoPath.3; SV1; .NET CLR 3.1.76908; WOW64; en-US)',
      'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; GTB7.4; InfoPath.2; SV1; .NET CLR 3.3.69573; WOW64; en-US)',
      'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)',
      'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; InfoPath.1; SV1; .NET CLR 3.8.36217; WOW64; en-US)',
      'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; .NET CLR 2.7.58687; SLCC2; Media Center PC 5.0; Zune 3.4; Tablet PC 3.6; InfoPath.3)',
      'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.2; Trident/4.0; Media Center PC 4.0; SLCC1; .NET CLR 3.0.04320)',
      'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 1.1.4322)',
      'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; InfoPath.2; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727)',
      'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
      'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; SLCC1; .NET CLR 1.1.4322)',
      'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.0; Trident/4.0; InfoPath.1; SV1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 3.0.04506.30)',
      'Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 5.0; Trident/4.0; FBSMTWB; .NET CLR 2.0.34861; .NET CLR 3.0.3746.3218; .NET CLR 3.5.33652; msn OptimizedIE8;ENUS)',
      'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.2; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0)',
      'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; Media Center PC 6.0; InfoPath.2; MS-RTC LM 8)',
      'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; Media Center PC 6.0; InfoPath.2; MS-RTC LM 8',
      'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; Media Center PC 6.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C)',
      'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.3; .NET4.0C; .NET4.0E; .NET CLR 3.5.30729; .NET CLR 3.0.30729; MS-RTC LM 8)',
      'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)',
      'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; Zune 3.0)'],
     'safari': ['Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A',
      'Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5355d Safari/8536.25',
      'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.13+ (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2',
      'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/534.55.3 (KHTML, like Gecko) Version/5.1.3 Safari/534.53.10',
      'Mozilla/5.0 (iPad; CPU OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko ) Version/5.1 Mobile/9B176 Safari/7534.48.3',
      'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; de-at) AppleWebKit/533.21.1 (KHTML, like Gecko) Version/5.0.5 Safari/533.21.1',
      'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_7; da-dk) AppleWebKit/533.21.1 (KHTML, like Gecko) Version/5.0.5 Safari/533.21.1',
      'Mozilla/5.0 (Windows; U; Windows NT 6.1; tr-TR) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27',
      'Mozilla/5.0 (Windows; U; Windows NT 6.1; ko-KR) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27',
      'Mozilla/5.0 (Windows; U; Windows NT 6.1; fr-FR) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27',
      'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27',
      'Mozilla/5.0 (Windows; U; Windows NT 6.1; cs-CZ) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27',
      'Mozilla/5.0 (Windows; U; Windows NT 6.0; ja-JP) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27',
      'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27',
      'Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_5_8; zh-cn) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27',
      'Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_5_8; ja-jp) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27',
      'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_7; ja-jp) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27',
      'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; zh-cn) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27',
      'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; sv-se) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27',
      'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; ko-kr) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27',
      'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; ja-jp) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27',
      'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; it-it) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27',
      'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; fr-fr) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27',
      'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; es-es) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27',
      'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; en-us) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27',
      'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; en-gb) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27',
      'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; de-de) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27',
      'Mozilla/5.0 (Windows; U; Windows NT 6.1; sv-SE) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4',
      'Mozilla/5.0 (Windows; U; Windows NT 6.1; ja-JP) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4',
      'Mozilla/5.0 (Windows; U; Windows NT 6.1; de-DE) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4',
      'Mozilla/5.0 (Windows; U; Windows NT 6.0; hu-HU) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4',
      'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4',
      'Mozilla/5.0 (Windows; U; Windows NT 6.0; de-DE) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4',
      'Mozilla/5.0 (Windows; U; Windows NT 5.1; ru-RU) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4',
      'Mozilla/5.0 (Windows; U; Windows NT 5.1; ja-JP) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4',
      'Mozilla/5.0 (Windows; U; Windows NT 5.1; it-IT) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4',
      'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4',
      'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-us) AppleWebKit/534.16+ (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4',
      'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; fr-ch) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4',
      'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_5; de-de) AppleWebKit/534.15+ (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4',
      'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_5; ar) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4',
      'Mozilla/5.0 (Android 2.2; Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4',
      'Mozilla/5.0 (Windows; U; Windows NT 6.1; zh-HK) AppleWebKit/533.18.1 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5',
      'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5',
      'Mozilla/5.0 (Windows; U; Windows NT 6.0; tr-TR) AppleWebKit/533.18.1 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5',
      'Mozilla/5.0 (Windows; U; Windows NT 6.0; nb-NO) AppleWebKit/533.18.1 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5',
      'Mozilla/5.0 (Windows; U; Windows NT 6.0; fr-FR) AppleWebKit/533.18.1 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5',
      'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-TW) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5',
      'Mozilla/5.0 (Windows; U; Windows NT 5.1; ru-RU) AppleWebKit/533.18.1 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5',
      'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; zh-cn) AppleWebKit/533.18.1 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5']}
    random_headers = [
    {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (X11; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36 OPR/56.0.3051.104'},
    {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36 OPR/54.0.2952.64'},
    {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0.2) Gecko/20100101 Firefox/58.0.2'},
    {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36 OPR/56.0.3051.104'},
    {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (X11; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36 OPR/57.0.3098.116'},
    {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (X11; Linux i686 on x86_64; rv:51.0) Gecko/20100101 Firefox/51.0'},
    {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.98 Safari/537.36'},
    {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:65.0) Gecko/20100101 Firefox/65.0'},
    {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'},
    {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1; rv:52.1.0) Gecko/20100101 Firefox/52.1.0'},
    ]
    browser = random.choice(list(random_user_agents.keys()))
    user_agent = random.choice(random_user_agents[browser])
    header = copy.copy(random.choice(random_headers))
    header['User-Agent'] = user_agent
    return header


def find_best_session():

    for i in range(10):
        try:
            # print('獲取新的Session 第', i, '回合')
            headers = generate_random_header()
            ses = requests.Session()
            ses.get('https://www.twse.com.tw/zh/', headers=headers, timeout=10)
            ses.headers.update(headers)
            # print('成功！')
            return ses
        except (ConnectionError, ReadTimeout) as error:
            # print(error)
            # print('失敗，10秒後重試')
            time.sleep(10)

    print('您的網頁IP已經被證交所封鎖，請更新IP來獲取解鎖')
    print("　手機：開啟飛航模式，再關閉，即可獲得新的IP")
    print("數據機：關閉然後重新打開數據機的電源")

date_range_record_file = os.path.join('history', 'date_range.pickle')

ses = None
def requests_get(*args1, **args2):

    # get current session
    global ses
    if ses == None:
        ses = find_best_session()

    # download data
    i = 3
    while i >= 0:
        try:
            return ses.get(*args1, timeout=10, **args2)
        except (ConnectionError, ReadTimeout) as error:
            time.sleep(60)
            ses = find_best_session()

        i -= 1
    return pd.DataFrame()

### ----------
###   Helper
### ----------

def otc_date_str(date):
    """將datetime.date轉換成民國曆

    Args:
        date (datetime.date): 西元歷的日期

    Returns:
        str: 民國歷日期 ex: 109/01/01
    """
    return str(date.year - 1911) + date.strftime('%Y/%m/%d')[4:]


def combine_index(df, n1, n2):

    """將dataframe df中的股票代號與股票名稱合併

    Keyword arguments:

    Args:
        df (pandas.DataFrame): 此dataframe含有column n1, n2
        n1 (str): 股票代號
        n2 (str): 股票名稱

    Returns:
        df (pandas.DataFrame): 此dataframe的index為「股票代號+股票名稱」
    """

    return df.set_index(df[n1].astype(str).str.replace(' ', '') + \
        ' ' + df[n2].astype(str).str.replace(' ', '')).drop([n1, n2], axis=1)

def crawl_benchmark(date):
    df=crawl_gitlab_backup('benchmark',date)
    if df is not None:
        return df
    else:
        date_str = date.strftime('%Y%m%d')
        res = requests_get("https://www.twse.com.tw/exchangeReport/MI_5MINS_INDEX?response=csv&date=" +
                           date_str + "&_=1544020420045")

        # 利用 pandas 將資料整理成表格

        if len(res.text) < 10:
            return pd.DataFrame()

        df = pd.read_csv(StringIO(res.text.replace("=","")), header=1, index_col='時間')

        # 資料處理

        df = df.dropna(how='all', axis=0).dropna(how='all', axis=1)
        df.index = pd.to_datetime(date.strftime('%Y %m %d ') + pd.Series(df.index))
        df = df.apply(lambda s: s.astype(str).str.replace(",", "").astype(float))
        df = df.reset_index().rename(columns={'時間':'date'})
        df['stock_id'] = '台股指數'
        return df.set_index(['stock_id', 'date'])

def crawl_capital():
    res = requests_get('https://dts.twse.com.tw/opendata/t187ap03_L.csv', )
    res.encoding = 'utf-8'
    df = pd.read_csv(StringIO(res.text))
    time.sleep(10)
    res = requests_get('https://dts.twse.com.tw/opendata/t187ap03_O.csv')
    res.encoding = 'utf-8'
    df = df.append(pd.read_csv(StringIO(res.text)))

    df['date'] = pd.to_datetime(str(datetime.datetime.now().year) + df['出表日期'].str[3:])
    df.set_index([df['公司代號'].astype(str) + ' ' + df['公司簡稱'].astype(str), 'date'], inplace=True)
    df.index.levels[0].name = '股票名稱'
    return df


def interest():
    res = requests_get('https://www.twse.com.tw/exchangeReport/TWT48U_ALL?response=open_data')
    res.encoding = 'utf-8'
    df = pd.read_csv(StringIO(res.text))

    time.sleep(10)

    res = requests_get('https://www.tpex.org.tw/web/stock/exright/preAnnounce/prepost_result.php?l=zh-tw&o=data')
    res.encoding = 'utf-8'
    df = df.append(pd.read_csv(StringIO(res.text)))

    df['date'] = df['除權息日期'].str.replace('年', '/').str.replace('月', '/').str.replace('日', '')
    df['date'] = pd.to_datetime(str(datetime.datetime.now().year) + df['date'].str[3:])
    df = df.set_index([df['股票代號'].astype(str) + ' ' + df['名稱'].astype(str), 'date'])
    return df


def preprocess(df, date):
    df = df.dropna(axis=1, how='all').dropna(axis=0, how='all')
    df.columns = df.columns.str.replace(' ', '')
    df.index.name = 'stock_id'
    df.columns.name = ''
    df['date'] = pd.to_datetime(date)
    df = df.reset_index().set_index(['stock_id', 'date'])
    df = df.apply(lambda s: s.astype(str).str.replace(',',''))

    return df



def bargin_twe(date):
    datestr = date.strftime('%Y%m%d')

    res = requests_get('https://www.twse.com.tw/fund/T86?response=csv&date='\
                       +datestr+'&selectType=ALLBUT0999')
    try:
        df = pd.read_csv(StringIO(res.text.replace('=','')), header=1)
    except:
        return pd.DataFrame()

    df = combine_index(df, '證券代號', '證券名稱')
    df = preprocess(df, date)
    return df

def bargin_otc(date):
    datestr = otc_date_str(date)

    url = 'https://www.tpex.org.tw/web/stock/3insti/daily_trade/3itrade_hedge_result.php?l=zh-tw&o=csv&se=EW&t=D&d='+datestr+'&s=0,asc'
    res = requests_get(url)
    try:
        df = pd.read_csv(StringIO(res.text), header=1)
    except:
        return pd.DataFrame()

    df = combine_index(df, '代號', '名稱')
    df = preprocess(df, date)
    return df

def price_twe(date):
    date_str = date.strftime('%Y%m%d')
    res = requests_get('https://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date='+date_str+'&type=ALLBUT0999')

    if res.text == '':
        return pd.DataFrame()

    header = np.where(list(map(lambda l: '證券代號' in l, res.text.split('\n')[:500])))[0][0]

    df = pd.read_csv(StringIO(res.text.replace('=','')), header=header-1)
    df = combine_index(df, '證券代號', '證券名稱')
    df = preprocess(df, date)
    return df

def price_otc(date):
    datestr = otc_date_str(date)
    link = 'https://www.tpex.org.tw/web/stock/aftertrading/daily_close_quotes/stk_quote_download.php?l=zh-tw&d='+datestr+'&s=0,asc,0'
    res = requests_get(link)
    df = pd.read_csv(StringIO(res.text), header=2)

    if len(df) < 30:
        return pd.DataFrame()

    df = combine_index(df, '代號', '名稱')
    df = preprocess(df, date)
    df = df[df['成交筆數'].str.replace(' ', '') != '成交筆數']
    return df

def pe_twe(date):
    datestr = date.strftime('%Y%m%d')
    res = requests_get('https://www.twse.com.tw/exchangeReport/BWIBBU_d?response=csv&date='+datestr+'&selectType=ALL')
    try:
        df = pd.read_csv(StringIO(res.text), header=1)
    except:
        return pd.DataFrame()

    df = combine_index(df, '證券代號', '證券名稱')
    df = preprocess(df, date)
    return df

def pe_otc(date):
    datestr = otc_date_str(date)
    res = requests_get('https://www.tpex.org.tw/web/stock/aftertrading/peratio_analysis/pera_result.php?l=zh-tw&o=csv&charset=UTF-8&d='+datestr+'&c=&s=0,asc')
    try:
        df = pd.read_csv(StringIO(res.text), header=3)
        df = combine_index(df, '股票代號', '名稱')
        df = preprocess(df, date)
    except:
        return pd.DataFrame()

    return df

def month_revenue(name, date):

    year = date.year - 1911
    month = (date.month+10)%12+1
    if month == 12:
        year -= 1
    url = 'https://mops.twse.com.tw/nas/t21/%s/t21sc03_%d_%d.html' % (name, year, month)
    print(url)
    res = requests_get(url, verify=False)
    res.encoding = 'big5'

    try:
        dfs = pd.read_html(StringIO(res.text), encoding='big-5')
    except Exception as e:
        print('MONTH ' + name + ': cannot parse ' + str(date))
        print(e)
        return pd.DataFrame()

    df = pd.concat([df for df in dfs if df.shape[1] <= 11 and df.shape[1] > 5])

    if 'levels' in dir(df.columns):
        df.columns = df.columns.get_level_values(1)
    else:
        df = df[list(range(0,10))]
        column_index = df.index[(df[0] == '公司代號')][0]
        df.columns = df.iloc[column_index]

    df = df.loc[:,~df.columns.isnull()]
    df = df.loc[~pd.to_numeric(df['當月營收'], errors='coerce').isnull()]
    df = df[df['公司代號'] != '合計']
    df = combine_index(df, '公司代號', '公司名稱')
    df = preprocess(df, datetime.date(date.year, date.month, 10))
    return df.drop_duplicates()

def crawl_split_twe():

    res = requests_get('https://www.twse.com.tw/exchangeReport/TWTAVU?response=csv&_=1537824706232')

    df = pd.read_csv(StringIO(res.text),header=1)
    df = df.dropna(how='all', axis=1).dropna(thresh=3, axis=0)

    def process_date(s):
        return pd.to_datetime(str(datetime.datetime.now().year) + s.str[3:])

    df['停止買賣日期'] = process_date(df['停止買賣日期'])
    df['恢復買賣日期'] = process_date(df['恢復買賣日期'])
    df['股票代號'] = df['股票代號'].astype(int).astype(str)
    df['stock_id'] = df['股票代號'] + ' ' + df['名稱']
    df['date'] = df['恢復買賣日期']
    df = df.set_index(['stock_id', 'date'])

    return df


def crawl_split_otc():
    res = requests_get("https://www.tpex.org.tw/web/stock/exright/decap/decap_download.php?l=zh-tw&d=107/09/21&s=0,asc,0")
    df = pd.read_csv(StringIO(res.text), header=1)
    df = df.dropna(thresh=5, axis=0)
    df['stock_id'] = df['代號'] + ' ' + df['名稱']
    def process_date(s):
        ss = s.astype(int).astype(str)
        return pd.to_datetime(str(datetime.datetime.now().year) + '/' + ss.str[3:5] + '/' + ss.str[5:])

    df['停止買賣日期'] = process_date(df['停止買賣日期'])
    df['恢復買賣日期'] = process_date(df['恢復買賣日期'])
    df['date'] = df['恢復買賣日期']
    df = df.rename(columns={'代號':'股票代號'})
    df = df.set_index(['stock_id', 'date'])
    return df

import io
import json
import requests
import datetime
import pandas as pd

def crawl_twse_divide_ratio():

    df=crawl_gitlab_backup('twse_divide_ratio')

    if df is not None:
        return df

    datestr = datetime.datetime.now().strftime('%Y%m%d')
    res = requests_get("https://www.twse.com.tw/exchangeReport/TWT49U?response=csv&strDate=20200101&endDate="+datestr)

    df = pd.read_csv(io.StringIO(res.text.replace("=", "")), header=1)
    df = df.dropna(thresh=5).dropna(how='all', axis=1)
    df = df[~df['資料日期'].isnull()]

    # set stock id
    df['stock_id'] = df['股票代號'] + ' ' + df['股票名稱']

    # set dates
    df = df[~df['資料日期'].isnull()]
    years = df['資料日期'].str.split('年').str[0].astype(int) + 1911

    #years.loc[df['資料日期'].str[3] != '年'] = np.nan
    years.loc[df['資料日期'].str.find('年') == -1] = np.nan

    years.loc[years > datetime.datetime.now().year] = np.nan
    years.ffill(inplace=True)
    dates = years.astype(int).astype(str) +'/'+ df['資料日期'].str.split('年').str[1].str.replace('月', '/').str.replace('日', '')
    df['date'] = pd.to_datetime(dates, errors='coerce')

    # convert to float
    float_name_list = ['除權息前收盤價', '除權息參考價', '權值+息值', '漲停價格',
                       '跌停價格', '開盤競價基準', '減除股利參考價' , '最近一次申報每股 (單位)淨值',
                       '最近一次申報每股 (單位)盈餘']

    df[float_name_list] = df[float_name_list].astype(str).apply(lambda s:s.str.replace(',', '')).astype(float)


    df['twse_divide_ratio'] = df['除權息前收盤價'] / df['開盤競價基準']
    return df.set_index(['stock_id', 'date'])

def crawl_otc_divide_ratio():

    df = crawl_gitlab_backup('otc_divide_ratio')

    if df is not None:
        return df

    y = datetime.datetime.now().year
    m = datetime.datetime.now().month
    d = datetime.datetime.now().day

    y = str(y-1911)
    m = str(m) if m > 9 else '0' + str(m)
    d = str(d) if d > 9 else '0' + str(d)

    datestr = '%s/%s/%s' % (y,m,d)
    res_otc = requests_get('https://www.tpex.org.tw/web/stock/exright/dailyquo/exDailyQ_result.php?l=zh-tw&d=109/01/02&ed=' + datestr)

    df = pd.DataFrame(json.loads(res_otc.text)['aaData'])
    df.columns = ['除權息日期', '代號', '名稱', '除權息前收盤價', '除權息參考價',
                      '權值', '息值',"權+息值","權/息","漲停價格","跌停價格","開盤競價基準",
                      "減除股利參考價","現金股利", "每千股無償配股", "現金增資股數", "現金增資認購價",
                      "公開承銷股數", "員工認購股數","原股東認購數", "按持股比例千股認購"]


    float_name_list = [ '除權息前收盤價', '除權息參考價',
                          '權值', '息值',"權+息值","漲停價格","跌停價格","開盤競價基準",
                          "減除股利參考價","現金股利", "每千股無償配股", "現金增資股數", "現金增資認購價",
                          "公開承銷股數", "員工認購股數","原股東認購數", "按持股比例千股認購"
    ]
    df[float_name_list] = df[float_name_list].astype(str).apply(lambda s:s.str.replace(',', '')).astype(float)

    # set stock id
    df['stock_id'] = df['代號'] + ' ' + df['名稱']

    # set dates
    dates = df['除權息日期'].str.split('/')
    dates = (dates.str[0].astype(int) + 1911).astype(str) + '/' + dates.str[1] + '/' + dates.str[2]
    df['date'] = pd.to_datetime(dates)

    df['otc_divide_ratio'] = df['除權息前收盤價'] / df['開盤競價基準']
    return df.set_index(['stock_id', 'date'])


def crawl_twse_cap_reduction():
    df=crawl_gitlab_backup('twse_cap_reduction')

    if df is not None:
        return df

    datestr = datetime.datetime.now().strftime('%Y%m%d')# 2011
    res3 = requests_get("https://www.twse.com.tw/exchangeReport/TWTAUU?response=csv&strDate=20200101&endDate=" + datestr + "&_=1551597854043")

    df = pd.read_csv(io.StringIO(res3.text), header=1)
    df = df.dropna(thresh=5).dropna(how='all',axis=1)

    dates = (df['恢復買賣日期'].str.split('/').str[0].astype(int) + 1911).astype(str) + df['恢復買賣日期'].str[3:]
    df['date'] = pd.to_datetime(dates, errors='coerce')
    df['stock_id'] = df['股票代號'].astype(int).astype(str) + ' ' + df['名稱']

    df['twse_cap_divide_ratio'] = df['停止買賣前收盤價格']/df['開盤競價基準']

    return df.set_index(['stock_id', 'date'])

def crawl_otc_cap_reduction():

    df=crawl_gitlab_backup('otc_cap_reduction')

    if df is not None:
        return df

    y = datetime.datetime.now().year
    m = datetime.datetime.now().month
    d = datetime.datetime.now().day

    y = str(y-1911)
    m = str(m) if m > 9 else '0' + str(m)
    d = str(d) if d > 9 else '0' + str(d)

    datestr = '%s/%s/%s' % (y,m,d)
    res4 = requests_get("https://www.tpex.org.tw/web/stock/exright/revivt/revivt_result.php?l=zh-tw&d=102/01/01&ed="+datestr)

    df = pd.DataFrame(json.loads(res4.text)['aaData'])

    name = ['恢復買賣日期', '股票代號', '股票名稱', '最後交易之收盤價格',
            '減資恢復買賣開始日參考價格', '漲停價格', '跌停價格', '開始交易基準價', '除權參考價', '減資源因', '詳細資料']

    float_name_list = ['最後交易之收盤價格', '減資恢復買賣開始日參考價格', '漲停價格', '跌停價格', '開始交易基準價', '除權參考價']
    df.columns = name
    df[float_name_list] = df[float_name_list].astype(str).apply(lambda s:s.str.replace(',', '')).astype(float)
    df['stock_id'] = df['股票代號'] + ' ' + df['股票名稱']
    dates = (df['恢復買賣日期'].astype(str).str[:-4].astype(int) + 1911).astype(str) + df['恢復買賣日期'].astype(str).str[-4:]
    df['date'] = pd.to_datetime(dates)
    df['date'] = pd.to_datetime(dates, errors='coerce')

    # calculate open price
    price = df['開始交易基準價'].copy()
    price[price == 0] = np.nan
    price.fillna(df['減資恢復買賣開始日參考價格'], inplace=True)

    df['otc_cap_divide_ratio'] = df['最後交易之收盤價格'] / price

    return df.set_index(['stock_id', 'date'])




o2tp = {'成交股數':'成交股數',
        '成交筆數':'成交筆數',
        '成交金額(元)':'成交金額',
        '收盤':'收盤價',
        '開盤':'開盤價',
        '最低':'最低價',
        '最高':'最高價',
        '最後買價':'最後揭示買價',
        '最後賣價':'最後揭示賣價',
      }

o2tpe = {
    '殖利率(%)':'殖利率(%)',
    '本益比':'本益比',
    '股利年度':'股利年度',
    '股價淨值比':'股價淨值比',
}

o2tb = {
    '外資及陸資(不含外資自營商)-買進股數':'外陸資買進股數(不含外資自營商)',
    '外資及陸資買股數': '外陸資買進股數(不含外資自營商)',

    '外資及陸資(不含外資自營商)-賣出股數':'外陸資賣出股數(不含外資自營商)',
    '外資及陸資賣股數': '外陸資賣出股數(不含外資自營商)',

    '外資及陸資(不含外資自營商)-買賣超股數':'外陸資買賣超股數(不含外資自營商)',
    '外資及陸資淨買股數': '外陸資買賣超股數(不含外資自營商)',

    '外資自營商-買進股數':'外資自營商買進股數',
    '外資自營商-賣出股數':'外資自營商賣出股數',
    '外資自營商-買賣超股數':'外資自營商買賣超股數',
    '投信-買進股數':'投信買進股數',
    '投信買進股數': '投信買進股數',
    '投信-賣出股數': '投信賣出股數',
    '投信賣股數': '投信賣出股數',

    '投信-買賣超股數':'投信買賣超股數',
    '投信淨買股數': '投信買賣超股數',

    '自營商(自行買賣)-買進股數':'自營商買進股數(自行買賣)',
    '自營商(自行買賣)買股數':'自營商買進股數(自行買賣)',

    '自營商(自行買賣)-賣出股數':'自營商賣出股數(自行買賣)',
    '自營商(自行買賣)賣股數':'自營商賣出股數(自行買賣)',

    '自營商(自行買賣)-買賣超股數': '自營商買賣超股數(自行買賣)',
    '自營商(自行買賣)淨買股數': '自營商買賣超股數(自行買賣)',

    '自營商(避險)-買進股數':'自營商買進股數(避險)',
    '自營商(避險)買股數': '自營商買進股數(避險)',
    '自營商(避險)-賣出股數':'自營商賣出股數(避險)',
    '自營商(避險)賣股數': '自營商賣出股數(避險)',
    '自營商(避險)-買賣超股數': '自營商買賣超股數(避險)',
    '自營商(避險)淨買股數': '自營商買賣超股數(避險)',

}

o2tm = {n:n for n in ['當月營收', '上月營收', '去年當月營收', '上月比較增減(%)', '去年同月增減(%)', '當月累計營收', '去年累計營收',
       '前期比較增減(%)']}

def merge(twe, otc, t2o):
    t2o2 = {k:v for k,v in t2o.items() if k in otc.columns}
    otc = otc[list(t2o2.keys())]
    otc = otc.rename(columns=t2o2)
    twe = twe[otc.columns & twe.columns]

    return twe.append(otc)


def crawl_price(date):

    df=crawl_gitlab_backup('price',date)

    if df is not None:
        return df

    dftwe = price_twe(date)
    time.sleep(5)
    dfotc = price_otc(date)
    if len(dftwe) != 0 and len(dfotc) != 0:
        df = merge(dftwe, dfotc, o2tp)
        return df
    else:
        return pd.DataFrame()


def crawl_bargin(date):

    df=crawl_gitlab_backup('bargin',date)

    if df is not None:
        return df

    dftwe = bargin_twe(date)
    dfotc = bargin_otc(date)
    if len(dftwe) != 0 and len(dfotc) != 0:
        return merge(dftwe, dfotc, o2tb)
    else:
        return pd.DataFrame()


def crawl_monthly_report(date):

    df=crawl_gitlab_backup('monthly_report',date)

    if df is not None:
        return df

    dftwe = month_revenue('sii', date)
    time.sleep(5)
    dfotc = month_revenue('otc', date)
    if len(dftwe) != 0 and len(dfotc) != 0:
        return merge(dftwe, dfotc, o2tm)
    else:
        return pd.DataFrame()

def crawl_pe(date):

    df=crawl_gitlab_backup('pe',date)

    if df is not None:
        return df

    dftwe = pe_twe(date)
    dfotc = pe_otc(date)
    if len(dftwe) != 0 and len(dfotc) != 0:
        return merge(dftwe, dfotc, o2tpe)
    else:
        return pd.DataFrame()

out = widgets.Output(layout={'border': '1px solid black'})

@out.capture()
def update_table(table_name, crawl_function, dates):

    if dates:
        if len(dates) == 0:
            print("該時間段沒有可以爬取之資料")
            return
        print('start crawl ' + table_name + ' from ', dates[0] , 'to', dates[-1])
    else:
        print('起始、結束日期有點怪怪的，請重新選擇一下喔，下載財報時，可以用以下的選法')
        print('第一季：該年 5/1~5/31')
        print('第二季：該年 8/1~8/31')
        print('第三季：該年 11/1~11/30')
        print('第四季：隔年 3/1~4/31')
        return


    df = pd.DataFrame()
    dfs = {}

    progress = tqdm_notebook(dates, )

    for d in progress:

        print('crawling', d, end="")
        progress.set_description('crawl' + table_name + str(d))

        data = crawl_function(d)

        if data is None or len(data) == 0:
            print('  ❌')

        # update multiple dataframes
        elif isinstance(data, dict):
            if len(dfs) == 0:
                dfs = {i:pd.DataFrame() for i in data.keys()}

            for i, d in data.items():
                dfs[i] = dfs[i].append(d)

        # update single dataframe
        else:
            df = df.append(data)
            print('  ✅')

        time.sleep(10)



    if df is not None and len(df) != 0:
        to_pickle(df, table_name)

    if len(dfs) != 0:
        for i, d in dfs.items():
            print('saveing df', d.head(), len(d))
            if len(d) != 0:
                print('save df', d.head())
                to_pickle(df, table_name)

import datetime
from dateutil.relativedelta import relativedelta

def check_monthly_revenue():

    df = pd.read_pickle("history/tables/monthly_report.pkl")

    if df.loc['1101 台泥', '2017-10-10']['當月營收'] == '8387381':
        print("fix monthly report errors")
        df = df.reset_index()
        df['date'] = [d + relativedelta(months=1) for d in df['date']]
        df.set_index(['stock_id', 'date'], inplace=True)
        df.to_pickle("history/tables/monthly_report.pkl")
        print("done")
        commit("monthly_report")

import pickle
def to_pickle(df, name):

    if not os.path.isdir('history'):
        os.mkdir('history')

    if not os.path.isdir(os.path.join('history', 'tables')):
        os.mkdir(os.path.join('history', 'tables'))


    fname = os.path.join('history', 'tables', name + '.pkl')
    newfname = os.path.join('history', 'tables', 'new' + name + '.pkl')

    # refine patch for monthly revenue

    if name == 'monthly_report' :
        check_monthly_revenue()

    if os.path.isfile(fname):
        old_df = pd.read_pickle(fname)
        old_df = old_df.append(df, sort=False)

        old_df = old_df[~old_df.index.duplicated(keep='last')]
        old_df = old_df.sort_index()
        old_df.to_pickle(newfname)
        os.remove(fname)
        os.rename(newfname, fname)
    else:
        df = df[~df.index.duplicated(keep='last')]
        df.to_pickle(fname)
        old_df = df

    if not os.path.isfile(date_range_record_file):
        pickle.dump({}, open(date_range_record_file, 'wb'))

    dates = pickle.load(open(date_range_record_file, 'rb'))
    dates[name] = (old_df.index.levels[1][0], old_df.index.levels[1][-1])
    pickle.dump(dates, open(date_range_record_file, 'wb'))

    commit(name)


from datetime import date
from dateutil.rrule import rrule, DAILY, MONTHLY

def date_range(start_date, end_date):
    return [dt.date() for dt in rrule(DAILY, dtstart=start_date, until=end_date)]

def month_range(start_date, end_date):
    return [dt.date() for dt in rrule(MONTHLY, dtstart=start_date, until=end_date)]

def season_range(start_date, end_date):

    if isinstance(start_date, datetime.datetime):
        start_date = start_date.date()

    if isinstance(end_date, datetime.datetime):
        end_date = end_date.date()

    ret = []
    for year in range(start_date.year-1, end_date.year+1):
        ret += [  datetime.date(year, 5, 15),
                datetime.date(year, 8, 14),
                datetime.date(year, 11, 14),
                datetime.date(year+1, 3, 31)]
    ret = [r for r in ret if start_date < r < end_date]

    return ret

import ipywidgets as widgets
from IPython.display import display

def table_date_range(table_name):
    if os.path.isfile(date_range_record_file):
        with open(date_range_record_file, 'rb') as f:
            dates = pickle.load(f)
            if table_name in dates:
                return dates[table_name]
            else:
                return [None, None]
    else:
        return [None, None]

from inspect import signature


def widget(table_name, crawl_func, range_date=None):


    sig = signature(crawl_func)

    if len(sig.parameters) == 0:
        @out.capture()
        def onupdate(x):
            print('updating ', table_name)
            df = crawl_func()
            to_pickle(df, table_name)
            print('done')

        btn = widgets.Button(description='update ')
        btn.on_click(onupdate)

        first_date, last_date = table_date_range(table_name)
        label = widgets.Label(table_name + ' | ' + str(first_date) + ' ~ ' + str(last_date))
        items = [btn]
        display(widgets.VBox([label, widgets.HBox(items)]))

    else:

        date_picker_from = widgets.DatePicker(
            description='from',
            disabled=False,
        )

        first_date, last_date = table_date_range(table_name)

        if last_date:
            date_picker_from.value = last_date

        date_picker_to = widgets.DatePicker(
            description='to',
            disabled=False,
        )

        date_picker_to.value = datetime.datetime.now().date()

        btn = widgets.Button(description='update ')

        def onupdate(x):
            dates = range_date(date_picker_from.value, date_picker_to.value)

            if len(dates) == 0:
                print('no data to parse')

            update_table(table_name, crawl_func, dates)

        btn.on_click(onupdate)


        label = widgets.Label(table_name + ' | ' + str(first_date) + ' ~ ' + str(last_date))

        items = [date_picker_from, date_picker_to, btn]
        display(widgets.VBox([label, widgets.HBox(items)]))

import requests
from io import StringIO
import pandas as pd
import numpy as np
from tqdm import tqdm_notebook as tqdm
import os
import pickle
import datetime
import random

def afterIFRS(year, season):
    season2date = [ datetime.datetime(year, 5, 15),
                    datetime.datetime(year, 8, 14),
                    datetime.datetime(year, 11, 14),
                    datetime.datetime(year+1, 3, 31)]

    return pd.to_datetime(season2date[season-1].date())

def clean(year, season, balance_sheet):

    if len(balance_sheet) == 0:
        return balance_sheet
    balance_sheet = balance_sheet.transpose().reset_index().rename(columns={'index':'stock_id'})


    if '會計項目' in balance_sheet:
        s = balance_sheet['會計項目']
        balance_sheet = balance_sheet.drop('會計項目', axis=1).apply(pd.to_numeric)
        balance_sheet['會計項目'] = s.astype(str)

    balance_sheet['date'] = afterIFRS(year, season)

    balance_sheet['stock_id'] = balance_sheet['stock_id'].astype(str)
    balance = balance_sheet.set_index(['stock_id', 'date'])
    return balance

def download_html(year, season, stock_ids, report_type='C'):

    directory = os.path.join('history', 'financial_statement', str(year) + str(season))
    if not os.path.exists(directory):
        os.makedirs(directory)

    files = [os.path.join(directory, str(i) + '.html') for i in stock_ids]
    pbar = tqdm([sid for file, sid in zip(files, stock_ids) if not os.path.exists(file) or os.stat(file).st_size < 10000])

    for sid in pbar:

        pbar.set_description('downloading stock %s in report type %s' % (sid, report_type))

        file = os.path.join(directory, str(sid) + '.html')

        # start parsing
        if int(year) >= 2013:
            url = ('https://mops.twse.com.tw/server-java/t164sb01?step=1&CO_ID=' + str(sid) + '&SYEAR=' + str(year) + '&SSEASON='+str(season)+'&REPORT_ID=' + str(report_type))
        else:
            url = ('https://mops.twse.com.tw/server-java/t147sb02?t203sb01Form=t203sb01Form&step=0&comp_id='+str(sid)+'&YEAR1='+str(year)+'&SEASON1='+str(season)+'&R_TYPE1=B')

        try:
            r = requests_get(url)
        except:
            print('**WARRN: requests cannot get stock:')
            print(url)
            continue

        r.encoding = 'big5'

        # write files
        f = open(file, 'w', encoding='utf-8')

        f.write('<meta charset="UTF-8">\n')
        f.write(r.text)
        f.close()

        # finish
        # print(percentage, i, 'end')

        # sleep a while
        time.sleep(random.uniform(5, 10))

import requests
import os
import time
import requests
import datetime
import random
import requests
import io
import shutil
import zipfile
import sys
import urllib.request



def crawl_finance_statement2019(year, season):

    def ifrs_url(year, season):
        url = "https://mops.twse.com.tw/server-java/FileDownLoad?step=9&fileName=tifrs-"+str(year)+"Q"+str(season)\
                +".zip&filePath=/home/html/nas/ifrs/"+str(year)+"/"
        print(url)
        return url



    from tqdm import tqdm
    class DownloadProgressBar(tqdm):
        def update_to(self, b=1, bsize=1, tsize=None):
            if tsize is not None:
                self.total = tsize
            self.update(b * bsize - self.n)


    def download_url(url, output_path):
        with DownloadProgressBar(unit='B', unit_scale=True,
                                 miniters=1, desc=url.split('/')[-1]) as t:
            urllib.request.urlretrieve(url, filename=output_path, reporthook=t.update_to)

    def download_file(url, filename):
        """
        Helper method handling downloading large files from `url` to `filename`. Returns a pointer to `filename`.
        """
        chunkSize = 1024
        r = requests.get(url, stream=True, verify=True)
        with open(filename, 'wb') as f:
            # pbar = tqdm( unit="B", total=int( r.headers['content-length'] ) )
            for chunk in r.iter_content(chunk_size=chunkSize):
                if chunk: # filter out keep-alive new chunks
                    # pbar.update (len(chunk))
                    f.write(chunk)
        return r

    def ifrs_url(year, season):
        url = "https://mops.twse.com.tw/server-java/FileDownLoad?step=9&fileName=tifrs-"+str(year)+"Q"+str(season)\
                +".zip&filePath=/home/html/nas/ifrs/"+str(year)+"/"
        print(url)
        return url

    url = ifrs_url(year,season)
    print('start download zip file from ', url)
    download_file(url, 'temp.zip')
    print('finished!')


    path = os.path.join('history', 'financial_statement', str(year) + str(season))

    if os.path.isdir(path):
        shutil.rmtree(path)

    zipfiles = zipfile.ZipFile(open('temp.zip', 'rb'))
    zipfiles.extractall(path=path)

    fnames = [f for f in os.listdir(path) if f[-5:] == '.html']
    fnames = sorted(fnames)

    newfnames = [f.split("-")[5] + '.html' for f in fnames]

    for fold, fnew in zip(fnames, newfnames):
        if len(fnew) != 9:
            os.remove(os.path.join(path, fold))
            continue

        if not os.path.exists(os.path.join(path, fnew)):
            os.rename(os.path.join(path, fold), os.path.join(path, fnew))
        else:
            os.remove(os.path.join(path, fold))


def crawl_finance_statement(year, season, stock_ids):

    directory = os.path.join('history', 'financial_statement', str(year) + str(season))
    if not os.path.exists(directory):
        os.makedirs(directory)

    if year >= 2013:
        download_html(year, season, stock_ids, 'C')
    download_html(year, season, stock_ids, 'B')
    download_html(year, season, stock_ids, 'A')

def remove_english(s):
    result = re.sub(r'[a-zA-Z()]', "", s)
    return result

def patch2019(df):
    df = df.copy()
    dfname = df.columns.levels[0][0]

    df = df.iloc[:,1:].rename(columns={'會計項目Accounting Title':'會計項目'})


    refined_name = df[(dfname,'會計項目')].str.split(" ").str[0].str.replace("　", "").apply(remove_english)

    subdf = df[dfname].copy()
    subdf['會計項目'] = refined_name
    df[dfname] = subdf

    df.columns = pd.MultiIndex(levels=[df.columns.levels[1], df.columns.levels[0]],codes=[df.columns.codes[1], df.columns.codes[0]])

    def neg(s):

        if isinstance(s, float):
            return s

        if str(s) == 'nan':
            return np.nan

        s = s.replace(",", "")
        if s[0] == '(':
            return -float(s[1:-1])
        else:
            return float(s)

    df.iloc[:,1:] = df.iloc[:,1:].applymap(neg)
    return df

def read_html2019(file):
    dfs = pd.read_html(file)
    return [pd.DataFrame(), patch2019(dfs[0]), patch2019(dfs[1]), patch2019(dfs[2])]


import re
def pack_htmls(year, season, directory):
    balance_sheet = {}
    income_sheet = {}
    cash_flows = {}
    income_sheet_cumulate = {}
    pbar = tqdm(os.listdir(directory))

    for i in pbar:

        # 將檔案路徑建立好
        file = os.path.join(directory, i)

        # 假如檔案不是html結尾，或是太小，代表不是正常的檔案，略過
        if file[-4:] != 'html' or os.stat(file).st_size < 10000:
            continue

        # 顯示目前運行的狀況
        stock_id = i.split('.')[0]
        pbar.set_description('parse htmls %d season %d stock %s' % (year, season, stock_id))

        # 讀取html
        if year < 2019:
            dfs = pd.read_html(file)
        else:
            try:
                dfs = read_html2019(file)
            except Exception as e:
                print("**ERROR: fail to parse ", file)
                print(e)
                continue

        # 處理pandas0.24.1以上，會把columns parse好的問題
        for df in dfs:
            if 'levels' in dir(df.columns):
                df.columns = list(range(df.values.shape[1]))

        # 假如html不完整，則略過
        if len(dfs) < 4:
            print('**WARRN html file broken', year, season, i)
            continue

        if year <= 2012:
            df = dfs[1]
            category = (df[0] == '會計科目').cumsum()
            df[category == 1]
            dfs = {
                1: df[category == 0],
                2: df[category == 1],
                3: df[category == 2],
            }

        # 取得 balance sheet
        df = dfs[1].copy().drop_duplicates(subset=0, keep='last')
        df = df.set_index(0)
        balance_sheet[stock_id] = df[1].dropna()
        #balance_sheet = combine(balance_sheet, df[1].dropna(), stock_id)

        # 取得 income statement
        df = dfs[2].copy().drop_duplicates(subset=0, keep='last')
        df = df.set_index(0)

        # 假如有4個columns，則第1與第3條column是單季跟累計的income statement
        if len(df.columns) == 4:
            income_sheet[stock_id] = df[1].dropna()
            income_sheet_cumulate[stock_id] = df[3].dropna()
        # 假如有2個columns，則代表第3條column為累計的income statement，單季的從缺
        elif len(df.columns) == 2:
            income_sheet_cumulate[stock_id] = df[1].dropna()

            # 假如是第一季財報 累計 跟單季 的數值是一樣的
            if season == 1:
                income_sheet[stock_id] = df[1].dropna()

        # 取得 cash_flows
        df = dfs[3].copy().drop_duplicates(subset=0, keep='last')
        df = df.set_index(0)
        cash_flows[stock_id] = df[1].dropna()

    # 將dictionary整理成dataframe
    balance_sheet = pd.DataFrame(balance_sheet)
    income_sheet = pd.DataFrame(income_sheet)
    income_sheet_cumulate = pd.DataFrame(income_sheet_cumulate)
    cash_flows = pd.DataFrame(cash_flows)

    # 做清理
    ret = {'balance_sheet':clean(year, season, balance_sheet), 'income_sheet':clean(year, season, income_sheet),
            'income_sheet_cumulate':clean(year, season, income_sheet_cumulate), 'cash_flows':clean(year, season, cash_flows)}

    # 假如是第一季的話，則 單季 跟 累計 是一樣的
    if season == 1:
        ret['income_sheet'] = ret['income_sheet_cumulate'].copy()

    ret['income_sheet_cumulate'].columns = '累計' + ret['income_sheet_cumulate'].columns

    pickle.dump(ret, open(os.path.join('history', 'financial_statement', 'pack' + str(year) + str(season) + '.pickle'), 'wb'))

    return ret

def get_all_pickles(directory):
    ret = {}
    for i in os.listdir(directory):
        if i[:4] != 'pack':
            continue
        ret[i[4:9]] = pd.read_pickle(os.path.join(directory, i))
    return ret

def combine(d):

    tnames = ['balance_sheet',
            'cash_flows',
            'income_sheet',
            'income_sheet_cumulate']

    tbs = {t:pd.DataFrame() for t in tnames}

    for i, dfs in d.items():
        for tname in tnames:
            tbs[tname] = tbs[tname].append(dfs[tname])
    return tbs


def fill_season4(tbs):
    # copy income sheet (will modify it later)
    income_sheet = tbs['income_sheet'].copy()

    # calculate the overlap columns
    c1 = set(tbs['income_sheet'].columns)
    c2 = set(tbs['income_sheet_cumulate'].columns)

    overlap_columns = []
    for i in c1:
        if '累計' + i in c2:
            overlap_columns.append('累計' + i)

    # get all years
    years = set(tbs['income_sheet_cumulate'].index.levels[1].year)

    for y in years:

        # get rows of the dataframe that is season 4
        ys = tbs['income_sheet_cumulate'].reset_index('stock_id').index.year == y
        ds4 = tbs['income_sheet_cumulate'].reset_index('stock_id').index.month == 3
        df4 = tbs['income_sheet_cumulate'][ds4 & ys].apply(lambda s: pd.to_numeric(s, errors='coerce')).reset_index('date')

        # get rows of the dataframe that is season 3
        yps = tbs['income_sheet_cumulate'].reset_index('stock_id').index.year == y - 1
        ds3 = tbs['income_sheet_cumulate'].reset_index('stock_id').index.month == 11
        df3 = tbs['income_sheet_cumulate'][ds3 & yps].apply(lambda s: pd.to_numeric(s, errors='coerce')).reset_index('date')

        if len(df3) == 0:
            continue
            
        # calculate the differences of income_sheet_cumulate to get income_sheet single season
        diff = df4 - df3
        diff = diff.drop(['date'], axis=1)[overlap_columns]

        # remove 累計
        diff.columns = diff.columns.str[2:]

        # 加上第四季的日期
        diff['date'] = pd.to_datetime(str(y) + '-03-31')
        diff = diff[list(c1) + ['date']].reset_index().set_index(['stock_id','date'])

        # 新增資料於income_sheet尾部
        income_sheet = income_sheet.append(diff)

    # 排序好並更新tbs
    income_sheet = income_sheet.reset_index().sort_values(['stock_id', 'date']).set_index(['stock_id', 'date'])
    tbs['income_sheet'] = income_sheet

def to_db(tbs):

    for i, df in tbs.items():
        df = df.reset_index().sort_values(['stock_id', 'date']).drop_duplicates(['stock_id', 'date']).set_index(['stock_id', 'date'])
        df.to_pickle(os.path.join('history', 'tables', i + '.pkl'))

    if not os.path.isfile(date_range_record_file):
        pickle.dump({}, open(date_range_record_file, 'wb'))

    dates = pickle.load(open(date_range_record_file, 'rb'))
    dates['financial_statement'] = (df.index.levels[1][0], df.index.levels[1][-1])
    pickle.dump(dates, open(date_range_record_file, 'wb'))


def html2db(year, season):

    pack_htmls(year, season, os.path.join('history', 'financial_statement', str(year) + str(season)))
    d = get_all_pickles(os.path.join('history', 'financial_statement'))
    tbs = combine(d)
    fill_season4(tbs)
    to_db(tbs)
    return {}

def crawl_finance_statement_by_date(date):
    year = date.year
    if date.month == 3:
        season = 4
        year = year - 1
        month = 11
    elif date.month == 5:
        season = 1
        month = 2
    elif date.month == 8:
        season = 2
        month = 5
    elif date.month == 11:
        season = 3
        month = 8
    else:
        return None

    if year < 2019:
        df = crawl_monthly_report(datetime.datetime(year, month, 1))
        crawl_finance_statement(year, season, df.index.levels[0].str.split(' ').str[0])
    else:
        crawl_finance_statement2019(year, season)

    html2db(year, season)
    commit()
    return {}


import os
import gc
import shutil
import pandas as pd
import numpy as np

def commit(*commit_tables):

    ftables = os.path.join('history', 'tables')
    fitems = os.path.join('history', 'items')

    fnames = [os.path.join(ftables, f) for f in os.listdir(ftables)]
    tnames = [f[:-4] for f in os.listdir(ftables)]

    if not os.path.isdir(fitems):
        os.mkdir(fitems)

    if len(commit_tables) == 0:
        commit_tables = tnames

    for fname, tname in zip(fnames, tnames):

        if tname not in commit_tables:
            continue

        if fname[-4:] != '.pkl':
            continue

        fdir = os.path.join(fitems, tname)

        if os.path.isdir(fdir) and os.path.getmtime(fname) < os.path.getmtime(fdir):
            print("已經成功commit過", tname, "了，跳過！")
            continue

        if os.path.isdir(fdir):
            shutil.rmtree(fdir)
            os.mkdir(fdir)
        else:
            os.mkdir(fdir)

        try:
            df = pd.read_pickle(fname)
        except:
            print("**檔案過大，無法成功commit", fname)
            continue

        # remove stock name
        df.reset_index(inplace=True)
        if sum(df['stock_id'].str.find(' ') >= 0) > 0:
            cond = df.stock_id.str[4] == ' '
            df = df[cond]
            gc.collect()
            df['stock_id'] = df['stock_id'].apply(lambda s:s[:s.index(' ')])


        df.set_index(['stock_id', 'date'], inplace=True)

        # select 4 digit stock ids
        if tname == 'price':
            sids = df.index.get_level_values(0)
            df = df[sids.str.len()==4]
            gc.collect()

        if tname == 'monthly_report':
            check_monthly_revenue()

        df = df.apply(lambda s: pd.to_numeric(s, errors='coerce'))
        gc.collect()

        df[df == 0] = np.nan


        df = df[~df.index.duplicated(keep='first')]
        gc.collect()

        items = list(df.columns)
        df.reset_index(inplace=True)

        df = df.pivot("date", "stock_id")
        gc.collect()

        for name, (_, series) in zip(items, df.items()):

            print(tname, '--', name)
            fitem = os.path.join(fdir, name.replace('+', '_').replace('/', '_'))
            #series.reset_index()\
            #    .pivot("date", "stock_id")[name].to_pickle(fitem + '.pkl')
            df[name].to_pickle(fitem + '.pkl')


import urllib.request
import pickle
import requests
from io import BytesIO


def crawl_gitlab_backup(target: str, date=None):
    crawlers_once_list = ['twse_divide_ratio', 'otc_divide_ratio', 'twse_cap_reduction', 'otc_cap_reduction']
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko)'
                      ' Chrome/39.0.2171.95 Safari/537.36'
    }

    if date is not None:
        date_str = date.strftime('%Y%m%d')
        if target == 'monthly_report':
            date_str = date.strftime('%Y%m')

    if target in crawlers_once_list:
        url = f'https://class.finlab.tw/data/{target}/{target}.pickle?inline=false'
    else:
        url = f'https://class.finlab.tw/data/{target}/{date_str}.pickle?inline=false'
    try:
        res = requests.get(url, headers=headers)
        df = pd.read_pickle(BytesIO(res.content))
        if 'stock_id' in df.columns and 'date' in df.columns:
            df.set_index(['stock_id', 'date'], inplace=True)
        return df
    except Exception as e:
        return None
