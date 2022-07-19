#!python3
# Date Detection
import re
import pyperclip

dateRegex = re.compile(r'''
    (\d\d)           # DAY   (0?[1-9]|[10-31])  
    \/
    (\d\d)           # MONTH   (0?[1-9]|[10-12]) 
    \/
    (\d\d\d\d)       # YEAR   
''', re.VERBOSE)

def isDateValid(day, month, year):
    isValid = True
    Dates = {
                1:'31', 2:'28', 3:"31", 4:'30', 5:"31", 6:"30",
                7:"31", 8:"31", 9:"30", 10:"31", 11:"30", 12:"31"
            }
    if not Dates.get(month):
        print("Month is invalid")
        isValid = False 
    elif month == 2:
        if not (year % 4 == 0 and not (year % 100 == 0) or year % 400 == 0 and day >0 and day <=29):
            print(formatDate(str(day), str(month), str(year)), "is not a leap year")
            isValid = False
    elif day <= 0 or day > int(Dates.get(month)):
        print("Day is invalid")
        isValid = False
    elif year < 1000 or year > 2999:
        print("Year is invalid")
        isValid = False    
    return isValid


def formatDate(day, month, year):
    return day + '/' + month + '/' + year

text = pyperclip.paste()


valid_dates = []
invalid_dates = []
for groups in dateRegex.findall(text):
    day, month, year = groups
    if isDateValid(int(day), int(month), int(year)):
        valid_dates.append(formatDate(day, month, year))
    else:
        invalid_dates.append(formatDate(day, month, year))

print("Valid dates: ")
print(valid_dates)
pyperclip.copy('\n'.join(valid_dates))
print("Copied to clipboard")
print("Invalid dates: ")
print(invalid_dates)
