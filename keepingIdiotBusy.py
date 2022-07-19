import pyinputplus as pyip 

answer = 'yes'
while answer == 'yes':
    answer = pyip.inputYesNo(prompt="Would you like to know how to keep a idiot busy for hours? ")
    
print("Thank you, have a nice day!")