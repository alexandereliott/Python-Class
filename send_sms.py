# Download the helper library from https://www.twilio.com/docs/python/install
"""The goal of this project is to write a program which will alert me via sms when my infrastructure or application has an issue."""
import os
from twilio.rest import Client
import secrets

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body='Hello sir, I am Gupta I saw your microsoft apple pro has a virus will you please install this vpn so I can fix it?',
         from_=secrets.from_number,
         to=secrets.to_number
     )

print(message.sid)

