from twilio.rest import Client
from twilio.rest import TwilioRestClient
from credentials import acc_sid, auth_token, my_cell, my_twilio


client = Client(acc_sid, auth_token)

my_msg = "Hello..."

message = client.messages.create(to=my_cell, from_=my_twilio,body=my_msg)
