# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 20:49:38 2022

@author: Hayes

"""
import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard.
    address = pyperclip.paste()
    

webbrowser.open('https://www.google.com/maps/place/' + address)