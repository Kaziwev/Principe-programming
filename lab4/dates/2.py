import datetime
Todaysdate=datetime.datetime.now()
Fiveday=datetime.timedelta(days=1)
Fivedayz=datetime.timedelta(months=1)
Subtraction=Todaysdate-Fiveday
Addition=Todaysdate+Fiveday
add=Todaysdate+Fivedayz
Today=Todaysdate.strftime("%Y/%m/%d")
Tomorrow=Addition.strftime("%Y/%m/%d")
Yesterday=Subtraction.strftime("%Y/%m/%d")
print(Today)
print(Tomorrow)
print(Yesterday)
print(add)