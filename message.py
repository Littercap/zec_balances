from twilio.rest import Client
accountSID = 'AC146fe4c95475b25af72d3633b225663e'
authToken = 'eb1feb256c0c7b01e0504208bfd3bcd8'
twilioCli = Client(accountSID,authToken)
myCellPhone = '+8613732255123'
myTwilioNumber = '+14159697232'
message = twilioCli.messages.create( body='Hello My Friend.', from_= myTwilioNumber, to= myCellPhone)
