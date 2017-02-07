#!/usr/bin/env bash

echo -e -n 'What is your username or email associated with Keybase: '
read user
curl -s https://keybase.io/_/api/1.0/getsalt.json?email_or_username=$user | python -c "import sys, json; print json.load(sys.stdin)['status']"
