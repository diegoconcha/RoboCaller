"""
Initiate phone call
https://www.twilio.com/docs/api/rest/making-calls
"""
from twilio import rest, TwilioRestException
 
def mC(account_sid,auth_token,target,ngrokURL):
    try:
        client = rest.TwilioRestClient(account_sid, auth_token)
         
        call = client.calls.create(ngrokURL,
                                   to=target,
                                   from_='+14157234236',
                                   if_machine='Continue') # experimental vm handling
    except TwilioRestException as e:
        print e