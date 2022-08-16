import datetime

print(datetime.datetime.now())
                    #   y    m   d   H   M   S
dt = datetime.datetime(2019, 10, 21, 16, 29, 0)

print(dt.year, dt.month, dt.day)

print(dt.hour, dt.minute, dt.second)

# Delta Tests
print('------timedelta data type ----')
delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
print(delta.days, delta.seconds, delta.microseconds)
print( delta.total_seconds())
print(str(delta))

print()

dt = datetime.datetime.now()
print(dt)

thousandDays = datetime.timedelta(days=1000)
print(dt + thousandDays)

print()
oct21st = datetime.datetime(2019, 10, 21, 16, 29, 0)

aboutThirtyYears = datetime.timedelta(days=365 * 30)
print(oct21st)
print(oct21st - aboutThirtyYears)
print(oct21st - (2 * aboutThirtyYears))

print()
print('-------strftime-----')
print(oct21st.strftime('%Y/%m/%d %H:%M:%S'))
print(oct21st.strftime('%I:%M %p'))
print( oct21st.strftime("%B of '%y"))

print()
print('-------strptime-----')
print(datetime.datetime.strptime('October 21, 2019', '%B %d, %Y'))
print(datetime.datetime.strptime('2019/10/21 16:29:00', '%Y/%m/%d %H:%M:%S'))
print(datetime.datetime.strptime("October of '19", "%B of '%y"))
print(datetime.datetime.strptime("November of '63", "%B of '%y"))