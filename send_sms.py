from twilio.rest import TwilioRestClient

account_sid =
auth_token = 
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(to="+14693283305", from = "+19703663441", body="Hello there!")

