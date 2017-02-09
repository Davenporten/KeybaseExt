#!/usr/bin/env bash

# Make request for initial vales needed for login
echo -e -n 'What is your username associated with Keybase: '
read user

# Python code here pulls out the needed values for logging in and passes it back to bash
initial_values=$(curl -s https://keybase.io/_/api/1.0/getsalt.json?email_or_username=$user | python -c "
import sys, json
initial = json.load(sys.stdin)  
if not 'salt' in initial:
    print 'Bad username (be sure NOT to use your email, this method is depreciated)\nEnding process'
    quit()
 
#needed_values = {'salt': initial['salt'], 'uid': initial['uid'], 'session': initial['login_session']}
for key in needed_values:
    print needed_values[key]")

echo $initial_values


