from twilio.rest import Client
from twilio.twiml.voice_response import Gather, VoiceResponse, Say

# put your own credentials here
account_sid = "AC0dbebc41c0d4125a118b5f5958fc3c81"
auth_token  = "290df12e2450cc200d9b1df988731e37"

# # set up a client to talk to the Twilio REST API
# client = Client(account_sid, auth_token)
#
# call = client.calls.create(to="+19494197775",    # to your cell phone
#                            from_="+14086693946", # from your Twilio phone number
#                            url="https://www.twilio.com/docs/twiml-snippet/quickstart")


class MakeCalls:

    @staticmethod
    def play_game():
        response = VoiceResponse()

        with response.gather(action='/handle_call/', method='POST') as g:
            g.say("Please enter number followed by pound")
        return response

    @staticmethod
    def fizz_buzz_value(data):
        message = str(data)
        if data % 5 == 0 and data % 3 == 0:
            message = "Fizz, Buzz"
        elif data % 3 == 0:
            message =  "Fizz"
        elif data % 5 == 0:
            message =  "Buzz"

        response = VoiceResponse()
        response.say(message)

        return response

