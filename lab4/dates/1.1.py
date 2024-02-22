import datetime
Todaysdate=datetime.datetime.now()
Fiveday=datetime.timedelta(days=5)
Year=Todaysdate.strftime("%Y")
Month=Todaysdate.strftime("%m")
Day=Todaysdate.strftime("%d")
Format=Year+"/"+Month+"/"+Day
print(Format)
