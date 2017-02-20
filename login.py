#!/usr/bin/env python 


try:
    __import__('scrypt')
    __import__('requests')
except:
    # Write more about how they might install it
    print ('The scrypt and requests modules are required, please install in your environment')
    quit()

import sys, json, scrypt, requests, getpass

user = input('What is your username associated with Keybase: ')
js = json.loads(requests.get('https://keybase.io/_/api/1.0/getsalt.json?email_or_username='+user).text)

if not js['status']['code'] is 0:
    print ('Bad username (be sure NOT to use your email, this method is depreciated)\nEnding process')
    quit()

salt = js['salt']
session = js['login_session']
pass_phrase = scrypt.hash(getpass.getpass('Keybase password (this cannot be accessed or stored outside of this script): '), salt, N=32768, r=8, p=1, buflen=256)

v4 = pass_phrase[194:224]
v5 = pass_phrase[224:256]

print (v4)
print (v5)
