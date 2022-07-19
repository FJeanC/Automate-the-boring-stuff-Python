import re

"""phoneRegex = re.compile(r'(\d{3}-)?\d{3}-\d{3}')

mo1 = phoneRegex.search("My number is 415-555-4242")

print(mo1.group())

mo2 = phoneRegex.search("My number is 555-4242")
print(mo2.group())
"""
'''
batRegex = re.compile(r'Bat(wo)+man')

mo1 = batRegex.search("The adventures of Batwoman")
print(mo1.group())'''
"""
haRegex = re.compile(r'(Ha){3,5}')
mo1 = haRegex.search('HaHaHaHaHa')
print(mo1.group())


haRegex = re.compile(r'(Ho)?(Ha){3,5}?')
mo1 = haRegex.search('HoHaHaHaHaHa')
print(mo1.group())"""


"""phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
teste = phoneNumRegex.findall("Cell 415-555-9999 work: 212-555-0000")
print(teste)"""

'''phoneNumRegex = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
teste = phoneNumRegex.findall("Cell 415-555-9999 work: 212-555-0000")
print(teste)'''

'''xMaxRegex = re.compile(r'\d+\s\w+')

teste = xMaxRegex.findall("12 drummers, 11 pipers, 10 lords")
print(teste)'''
"""
regex = re.compile(r'robocop', re.I)

print(regex.search('RoBoCop is part man, part machine, all cop').group())
"""

"""agentNames = re.compile(r'Agent (\w)\w*')
print(agentNames.sub(r'\1****', 'Agent Alice told Agent Carol that Agent eve Knew Agent Bob was a double agent.'))"""

"""phoneRegex = re.compile(r'''
    ((\d{3}|\(\d{3}\))?           #area coce
    (\s|-|\.)?                   #separator 
    \d{3}                        #first 3 digits
    (\s|-|\.)                    #separator 
    \d{4}                        #last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})? #extension
)''', re.VERBOSE)

mo = phoneRegex.search("My number is (123)442-1234")
print(mo.group())"""

"""someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)"""
