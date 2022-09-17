import os
from twilio.rest import Client

account_sid = os.environ['account_sid']
auth_token = os.environ['auth_token']

client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Yay! Push event triggered in master branch',
                              from_='whatsapp:+14155238886',
                              to='whatsapp:'+os.environ['to_whatsapp_no']
                          )

print("Message ID:",message.sid)
- isim: Özel mesajlarla Whatsapp'ta push bildirimi
  kullanım alanları: KhaledAhmed-Ibtikar/whatsapp-push-notify-action@1.3
