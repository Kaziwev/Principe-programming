import datetime
Todaysdate=datetime.datetime.now()
Fiveday=datetime.timedelta(days=5)
hi=Fiveday.strftime("%Y/%m/%d")
today=Todaysdate.strftime("%Y/%m/%d")
hu=today+Fiveday
print(hu)