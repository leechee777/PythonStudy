# coding=utf-8

import tushare as ts
ts.set_token('67450e7fd80710fbc4b64d1910ef242569fc754f93d71bd21c276fa8')
pro = ts.pro_api()
fileNmae = 'sotck.csv'
df = pro.trade_cal(exchange='', start_date='20180901', end_date='20181001', fields='exchange,cal_date,is_open,pretrade_date', is_open='0')
print(df)
# stockList.to_csv(fileNmae)