from datetime import datetime
from apscheduler.scheduler import Scheduler
import time

# Start the scheduler
sched = Scheduler()
sched.start()

# Define the function that is to be executed
def my_job(text):
    print text

# The job will be executed on November 6th, 2009
exec_date = datetime(2014,04,22,13,19,30)

# Store the job in a variable in case we want to cancel it
job = sched.add_date_job(my_job, exec_date, ['Hello Monkey!'])

# Have to keep script running otherwise the scheduler will die (end it by Ctrl+C)
# http://stackoverflow.com/questions/5835600/apscheduler-not-starting
while True:
    time.sleep(1)
sched.shutdown()