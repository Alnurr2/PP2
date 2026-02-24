import datetime
from datetime import timedelta

today = datetime.datetime.now()

drop = today.replace(microsecond=0)
print(drop)

