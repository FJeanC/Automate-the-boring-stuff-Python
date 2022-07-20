#! python3
# mapit.py - Launches a map in the browser using an adress 
# from the command line or clipboard

import webbrowser
import sys
import pyperclip

if len(sys.argv) > 1:
    # Get adresses from command line.
    address = ' '. join(sys.argv[1:])

else:
    # Get adress from clipboard.
    address = pyperclip.paste()

webbrowser.open('https://google.com/maps/place/'+ address)
