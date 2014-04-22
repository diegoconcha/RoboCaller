RoboCaller
==========

Code Challenge Project

At a specific UTC time, it grabs the top headline from Reddit.com, calls a number, and says my name, the headline, and goodbye.
It uses Twilio's REST API, Twilio's text-to-speech library, urllib2, ngrok, flask, apscheduler, and fancy UTC to local datetime conversions.


Requirements:
1. Register an account on ngrok.com
2. Download ngrok and unzip to the local project directory.
3. A csv file in the local project directory called 'auth.txt' with the Twilio account_sid and auth_token:
account_sid,'...'
auth_token,'...'
4. Be sure to change hardcoded targetNumber, targetUTCTime, and ngrokURL in main.py using the same formats.

To run do:
python main.py

Future versions will not have the hardcodded values.
