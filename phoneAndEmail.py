#! python 3
# Finds phone number and email address on the clipboard

from operator import add
import re, pyperclip

phoneRegex = re.compile(r'''(
        (\d{3}|\(\d{3}\))?              # area code
        (\s|-|\.)?                      # separator
        (\d{3})                         # first 3 digits
        (\s|-|\.)                       # separator
        (\d{4})                         # last 4 digits
        (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension
    )''', re.VERBOSE)

phoneRegexBrazil = re.compile(r'''
    (\d{2}|\(\d{2}\))      #DDD
    (\s*)?                 #Espaço ou não
    (\d{4,5})              #4 numeros pra fixo ou 5 pra celular
    (\s|-|\.)?             #separador
    (\d{4})                #4 ultimos digitos
    ''', re.VERBOSE)

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+       #username
    @                       # @
    [a-zA-z0-9.-]+          # domain name
    (\.[a-zA-z]{2,4})       # dot-something
    )''', re.VERBOSE)

text = str(pyperclip.paste())

matches = list()

americanNumbers = None

americanNumbers = input("Find brazilian phone numbers(type 1) or american phone numbers (type 2):")
match americanNumbers:
    case '1':
        for groups in phoneRegexBrazil.findall(text):
            addParenthesis = groups[0]
            if '(' and ')' not in groups[0]:
                addParenthesis = '('+addParenthesis+')'
            phoneNum = ' '.join([addParenthesis, groups[2]])
            phoneNum = phoneNum + '-' + groups[4]
            matches.append(phoneNum)

    case '2':
        for groups in phoneRegex.findall(text):
            phoneNum = '-'.join([groups[1], groups[3], groups[5]])
            if groups[8] != '':
                phoneNum += ' x' + groups[8]
            matches.append(phoneNum)

    case _:
        print("Finding only emails")



for groups in emailRegex.findall(text):
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print("Copied to clipboard")
    print('\n'.join(matches))
else:
    print("No phone numbers or email adresses found.")



