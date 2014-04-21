from twilio.rest import TwilioRestClient
 
account_sid = raw_input("Account SID:")
auth_token = raw_input("Auth Token:")
target = raw_input("Target (eg. +13334445555):")

client = TwilioRestClient(account_sid, auth_token)

call = client.calls.create(to=target,
                           from_="+14157234236",
                           url="http://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient")
#print call.sid