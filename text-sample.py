from twilio.rest import TwilioRestClient

# Get SID and AuthToken
account_sid = raw_input("Account SID:")
auth_token = raw_input("Auth Token:")

# Send text
try:
    client = TwilioRestClient(account_sid, auth_token)
    target = raw_input("Target (eg. +13334445555):")
    message = client.messages.create(
        body="Hey there sexy ;)",
        to=target,
        from_="+14157234236"
    )
#    print message.sid
except twilio.TwilioRestException as e:
    print e