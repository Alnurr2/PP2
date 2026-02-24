from datetime import timedelta
import datetime


x = datetime.datetime.now()
print(x)

sub = x - datetime.timedelta(days=5)
print(sub)