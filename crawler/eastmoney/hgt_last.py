# coding: utf-8

import requests
import re
import time
from datetime import datetime
import logging


def fetch_hgt():
    eastmoney_data_url = 'http://datainterface.eastmoney.com/EM_DataCenter/JS.aspx?type=DPAB&sty=AHTZJL'
    r = requests.get(eastmoney_data_url)
    hk_to_sh_text = r.text[3:-3].split(',')[3]
    number_text = re.findall('[\d\.-]+', hk_to_sh_text)[0]
    number = float(number_text)
    hk_to_sh_money = 0
    if u'亿' in hk_to_sh_text:
        hk_to_sh_money = number * 10000 * 10000
    elif u'万' in hk_to_sh_text:
        hk_to_sh_money = number * 10000
    return hk_to_sh_text, hk_to_sh_money


while True:
    now = datetime.now()
    try:
        hgt = fetch_hgt()
        print datetime.strftime(now, '%Y-%m-%d %H:%M:%S'), hgt[0], hgt[1]
        time.sleep(30)
    except Exception as e:
        logging.warning(e)

