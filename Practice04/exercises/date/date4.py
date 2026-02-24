import datetime
from datetime import timedelta

today = datetime.datetime.now()
time = datetime.datetime(2025,12,5,3,4,34)
drop = today.second - time.second
print(today.second)
print(drop)

