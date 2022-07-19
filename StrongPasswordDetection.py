#python3
# Strong password Detection

import re

testRegex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$')

password = input("Type the password: ")

mo = testRegex.search(password)
if mo == None:
    print("Weak Password")
else:
    print(mo.group())
    print("Strong password")