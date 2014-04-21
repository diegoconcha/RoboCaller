"""
Initiate phone call
https://www.twilio.com/docs/api/rest/making-calls
"""
from twilio import rest, TwilioRestException
 
def mC(account_sid,auth_token,target):
    try:
        client = rest.TwilioRestClient(account_sid, auth_token)
         
        call = client.calls.create(url='http://rcxml.ngrok.com',
                                   to=target,
                                   from_='+14157234236',
                                   if_machine='Continue') # experimental vm handling
    except TwilioRestException as e:
        print e