import datetime

Todaysdate = datetime.datetime.now()
Fiveday = datetime.timedelta(days=1)
Subtraction = Todaysdate - Fiveday
Addition = Todaysdate + Fiveday

Today = Todaysdate.strftime("%Y/%m/%d")
Tomorrow = Addition.strftime("%Y/%m/%d")
Yesterday = Subtraction.strftime("%Y/%m/%d")


TodayDateTime = datetime.datetime.strptime(Today, "%Y/%m/%d")


DifferenceInSeconds = (TodayDateTime - Subtraction).total_seconds()

print("Today:", Today)
print("Tomorrow:", Tomorrow)
print("Yesterday:", Yesterday)
print("Difference in seconds between Today and Subtraction:", DifferenceInSeconds)