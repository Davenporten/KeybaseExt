#!/usr/bin/env python 


try:
    __import__('scrypt')
    __import__('requests')
except:
    # Write more about how they might install it
    print ('The scrypt and requests modules are required, please install in your environment')
    quit()

import json, scrypt, requests, getpass, random, string

def nonce_gen(length):
    return ''.join([str(random.SystemRandom().choice(string.ascii_lowercase + string.digits)) for i in range(length)])

user = input('What is your username associated with Keybase: ')
js = json.loads(requests.get('https://keybase.io/_/api/1.0/getsalt.json?email_or_username='+user).text)

if not js['status']['code'] is 0:
    print ('Bad username (be sure NOT to use your email, this method is depreciated)\nEnding process')
    quit()

# Need better way to parse public key
pub_key = requests.get('https://keybase.io/'+user+'/key.asc').text.split('\n')
if pub_key[0].split(' ', 1)[0] == '404':
    print ('There is no public key associated with this username.')
    quit()

salt = js['salt']
session = js['login_session']
pass_phrase = scrypt.hash(getpass.getpass('Keybase password (this cannot be accessed or stored outside of this script): '), salt, N=32768, r=8, p=1, buflen=256)

v4 = pass_phrase[194:224]
v5 = pass_phrase[224:256]
nonce = nonce_gen(32)

print (v4)
print (v5)
print (nonce)
