"""
Get the title text from the top story on Reddit.com
and return it as a string
https://docs.python.org/2.7/howto/urllib2.html
"""
from urllib2 import urlopen, URLError
import bs4

def gH():
    try:
        response = urlopen("http://www.reddit.com/")
    except URLError as e:
        if hasattr(e, 'reason'):
            return 'ERROR: We failed to reach a server.\nReason: %s' % e.reason
        elif hasattr(e, 'code'):
            return 'ERROR: The server couldn\'t fulfill the request.\nError code: %s' % e.code
    else:
        dom = bs4.BeautifulSoup(response.read())
        a = dom.select("div.content div.spacer #siteTable p.title a.title")[0]
        title = a.get_text()
        return title