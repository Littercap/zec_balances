from twilio.rest import Client
accountSID = ''
authToken = ''
twilioCli = Client(accountSID,authToken)
myCellPhone = '+'
myTwilioNumber = '+14159697232'
message = twilioCli.messages.create( body='Hello My Friend.', from_= myTwilioNumber, to= myCellPhone)
