"""
Python Flask Web Server
https://www.twilio.com/docs/quickstart/python/client/hello-monkey
"""
from flask import Flask
import twilio.twiml

app = Flask(__name__)
 
@app.route("/", methods=['GET', 'POST'])
def message():
    """Respond to incoming requests."""
    resp = twilio.twiml.Response()
    resp.say("Hello Monkey")
 
    return str(resp)
 
if __name__ == "__main__":
    app.run(debug=True)