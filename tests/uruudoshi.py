from calendar import isleap

year_list = [2000, 2019, 2020, 2021, 2100]
for year in year_list:
    result = isleap(year)
    print(f'{year} is a leap year: {result}')
# 出力結果：
#2000 is a leap year: True
#2019 is a leap year: False
#2020 is a leap year: True
#2021 is a leap year: False
#2100 is a leap year: False

def isleapyear(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

for year in year_list:
    result = isleapyear(year)
    print(f'{year} is a leap year: {result}')
# 出力結果は上に同じ

# datetimeオブジェクト、time.struct_timeオブジェクトを対象に判定する
from datetime import datetime
import time

dt = datetime.now()
result = isleap(dt.year)
print(f'{dt.year} is a leap year: {result}') # 2021 is a leap year: False

d = time.localtime()
result = isleap(d.tm_year)
print(f'{d.tm_year} is a leap year: {result}')  # 2021 is a leap year: False

years_datetime_type = [datetime(year=y, month=1, day=1) for y in year_list]
for d in years_datetime_type:
    result = isleap(d.year)
    print(f'{d.year} is a leap year: {result}')

years_str_time = [datetime.timetuple(y) for y in years_datetime_type]
for d in years_str_time:
    result = isleap(d.tm_year)
    print(f'{d.tm_year} is a leap year: {result}')