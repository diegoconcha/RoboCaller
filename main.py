"""
Using Python, write code to use the Twilio API to automatically call
my cell phone at 6:00pm UTC time on Tuesday (4/22),
and read me (a) your name and (b) the top headline on the front page
of Reddit. Some time after I receive the call, email me the code and
a brief description of your solution.

To launch HTTP tunneling:
./ngrok -subdomain rcxml 5000

To launch webserver:
python runServer.py
"""
import sys
from grabHeadline import gH
from parseCSV import pF
from makeCall import mC

filename = 'auth.txt'
#target ='+16175130992'
target ='+13057209243'

# Parse csv auth file
auth = pF(filename)

# Get headline string
headline = gH()

if (headline.find('ERROR') != -1):
    sys.exit(headline)

# Pass headline to webserver

# Make call with Twilio
mC(auth['account_sid'],auth['auth_token'],target)

print "Call scheduled"