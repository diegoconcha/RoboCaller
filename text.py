import twilio

# Send text
try:
    client = twilio.rest.TwilioRestClient(account_sid, auth_token)
 
    message = client.sms.messages.create(
        body="Hey there sexy ;)",
        to="+13057209243",
        from_=""
    )
except twilio.TwilioRestException as e:
    print e