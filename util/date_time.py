# coding: utf-8

chinese_holidays = [
    '2016-01-01',
    '2016-02-07', '2016-02-08', '2016-02-09', '2016-02-10', '2016-02-11', '2016-02-12', '2016-02-13',
    '2016-04-04',
    '2016-05-01', '2016-05-02',
    '2016-06-09', '2016-06-10',
    '2016-09-15', '2016-09-16',
    '2016-10-03', '2016-10-04', '2016-10-05', '2016-10-06', '2016-10-07'
]


def is_holiday_day(date_):
    return date_.isoweekday() in [6, 7] or date_.strftime('%Y-%m-%d') in chinese_holidays


def is_trade_day(date_):
    return not is_holiday_day(date_)
