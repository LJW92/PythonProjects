from twilio.rest import Client

S_ID = "AC53bc84328301e9a2e40bda921b3be8c1"
TOKEN = "9929c38e60027c5fd9e34eea757732f1"


def notify_me(text):
    client = Client(S_ID, TOKEN)
    message = client.messages.create(
        body=text,
        from_="+12512374840",
        to='+61450180802'
    )
    print(message.status)


class NotificationManager:

    def __init__(self):
        pass
