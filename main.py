"""
Using Python, write code to use the Twilio API to automatically call
my cell phone at 6:00pm UTC time on Tuesday (4/22),
and read me (a) your name and (b) the top headline on the front page
of Reddit. Some time after I receive the call, email me the code and
a brief description of your solution.
"""
import urllib2
import bs4

# Get the title text from the top story on Reddit.com
response = urllib2.urlopen("http://www.reddit.com/")
dom = bs4.BeautifulSoup(response.read())
a = dom.select("div.content div.spacer #siteTable p.title a.title")[0]
title = a.get_text()

# Create object for Twilio


# Schedule call with Twilio
