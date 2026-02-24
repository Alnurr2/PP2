import datetime 

x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))


y = datetime.datetime(2022,4,23)
print(y.strftime("%A"))