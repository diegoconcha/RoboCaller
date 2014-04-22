"""
Python Flask Web Server
https://www.twilio.com/docs/quickstart/python/client/hello-monkey
http://flask.pocoo.org/docs/quickstart/#quickstart
"""
from flask import Flask
from grabHeadline import gH
import twilio.twiml

app = Flask(__name__)
 
@app.route("/", methods=['GET', 'POST'])
def index():
    resp = twilio.twiml.Response()
    headline = gH()
    if (headline.find('ERROR') != -1):
        sys.exit(headline)

    resp.say(headline)

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
