
# 导入tushare
import tushare as ts

# 初始化pro接口
pro = ts.pro_api('bacea3bcf3f7e068888c0a1b16a683a1f972337b6329209a499623a9')

df = pro.daily(ts_code='002240.SZ,603050.SH', start_date='20220801', end_date='20220831')


print(df)
