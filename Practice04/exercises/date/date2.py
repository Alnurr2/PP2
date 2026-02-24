import datetime
from datetime import timedelta

today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days=1)
print(yesterday,end="\n")
print(today,end="\n")
print(tomorrow,end="\n") 