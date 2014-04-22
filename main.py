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

https://docs.python.org/2.7/library/subprocess.html#using-the-subprocess-module
http://pythonhosted.org/APScheduler/dateschedule.html
http://stackoverflow.com/questions/5835600/apscheduler-not-starting
"""
import sys, subprocess, time, os
from datetime import datetime
from apscheduler.scheduler import Scheduler
from parseCSV import pF
from makeCall import mC

filename = 'auth.txt'
#target ='+16175130992'
target ='+13057209243'

def main(filename,target):
    # Parse csv auth file
    auth = pF(filename)

    # Launch ngrok
    ngrok = subprocess.Popen('./ngrok -subdomain rcxml 5000', shell=True)
    print 'ngrok PID: %s' % ngrok.pid

    # Launch webserver
    server = subprocess.Popen('python runServer.py', shell=True)
    print 'Server PID: %s' % server.pid

    # Make call with Twilio API
    mC(auth['account_sid'],auth['auth_token'],target)

    print "Call Queued Up"

    time.sleep(60) # Twilio default call timeout is 60 sec
    #kill = raw_input("Kill proceses? (y/n):")
    #while kill in ['n']:
    #    kill = raw_input("Kill proceses? (y/n):")

    print "Killing processes"
    ngrok.kill() # kill ngrok process
    os.system('killall -KILL Python') # kill web server and this thread

# Start the scheduler
sched = Scheduler()
sched.start()

job = sched.add_date_job(main, datetime(2014, 4, 22, 13, 24, 0), [filename,target])

sched.print_jobs()

# Keep scheduler alive until you hit Ctrl+C!
while True:
    time.sleep(1)
sched.shutdown()
