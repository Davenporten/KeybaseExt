#!/usr/bin/env bash

# Make request for initial vales needed for login
t1=$(which python3)
if [ "$t1" == "" ]
  then
    echo "python3 is required, please install in your environment."
    exit
fi

t2=$(python3 -c "
try:
    __import__('scrypt')
except:
    print (1)")
if [ "$t2" == "1" ]
  then
    echo "scrypt is required, please install in your environment."
fi

echo -e -n 'What is your username associated with Keybase: '
read user

# Python code here pulls out the needed values for logging in and passes it back to bash
initial_values=$(curl -s https://keybase.io/_/api/1.0/getsalt.json?email_or_username=$user | python3 -c "
import sys, json, scrypt
initial = json.load(sys.stdin)  
if not 'salt' in initial:
    print ('Bad username (be sure NOT to use your email, this method is depreciated)\nEnding process')
    quit()
# salt, session, uid
#needed_values = initial['salt']+' '+initial['login_session']+' '+initial['uid']
salt = initial['salt']
session = initial['login_session']
")

echo $initial_values


