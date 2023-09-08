from twilio.rest import Client
import smtplib
TWILIO_SID = "AC53bc84328301e9a2e40bda921b3be8c1"
TWILIO_AUTH_TOKEN = "9929c38e60027c5fd9e34eea757732f1"
TWILIO_VIRTUAL_NUMBER = "+12512374840"
TWILIO_VERIFIED_NUMBER = "+61450180802"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)


    def send_emails(self, emails, message):
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login('lijiaweipython@gmail.com', 'ajnqjljoqbhfhcuu')
            for email in emails:
                connection.sendmail(
                    from_addr='lijiaweipython@gmail.com',
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}".encode('utf-8')
                )