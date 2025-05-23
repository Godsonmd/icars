import random
from twilio.rest import Client
from django.conf import settings

def send_otp(phone_number):
    otp = random.randint(100000, 999999)  # Generate a 6-digit OTP
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

    message = client.messages.create(
        body=f"Your OTP is: {otp}",
        from_=settings.TWILIO_PHONE_NUMBER,
        to=phone_number
    )
    
    return otp 