"""
Get local time target from a UTC time target
http://stackoverflow.com/questions/4770297/python-convert-utc-datetime-string-to-local-datetime
"""
import time
from datetime import datetime

def utc2local (utc):
    epoch = time.mktime(utc.timetuple()) # i.e. unix time of utc target
    # Calculate difference between local and UTC
    offset = datetime.fromtimestamp(epoch) - datetime.utcfromtimestamp(epoch)
    return utc + offset # convert to local