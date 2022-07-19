#python3
# A regex function that does the same as strip()

import re

# regexStrip = re.compile(r'[^\s]+[a-zA-Z0-9][^\s]')
# regexStrip = re.compile(r'[^\s]+.+[^\s]')

def regexStrip(*args):
    rule = re.compile(r'[^\s]+.+[^\s]')
    match len(args):
        case 1:
            return rule.search(args[0]).group()
        case 2:
            return args[0].replace(args[1], '')

phrase = input("Type a string: ")

character = input("If you would like to remove a character, type it.Otherwise, press enter: ")

if len(character) == 0:
    result = regexStrip(phrase)
else:
    result = regexStrip(phrase, character)
print(result)