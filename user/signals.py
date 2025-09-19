from .models import User
from utils.index import send_smtp_mail
from .models import PasswordReset
from django.dispatch import receiver
from django.db.models.signals import post_save



@receiver(post_save, sender=User)
def send_mail_for_subscription_with_template(sender, instance, created, **kwargs):

    if created:
        recipient = instance.email
        first_name = instance.first_name
        last_name = instance.last_name

        subject = "🎉 Welcome to Our App"
        from_email = "micode360@gmail.com"
        to=[recipient]

        send_smtp_mail(
            subject,
            from_email,
            to,
            {
                "header": f"{first_name} {last_name}",
                "description": "We are glad to have you with us.",
                "extra_info": "Let’s get started 🚀 The app is a tutorial app.",
                "otp": None,
                "show_button": True,
                "button_text": "Get started",
                "button_link": "http://localhost:3000/onboarding"
            }
        )



# Sending OTP after otp is saved
@receiver(post_save, sender=PasswordReset)
def send_otp_email(sender, instance, created, **kwargs):
    if created:  
        recipient = instance.email

        subject = "Your OTP Code"
        from_email = "micode360@gmail.com"
        to=[recipient]

        send_smtp_mail(
            subject,
            from_email,
            to,
            {
                "header": "Your OTP Code",
                "description": "Use the one-time password (OTP) below to verify your account.",
                "otp": "483920", 
                "extra_info": "This OTP is valid for 10 minutes.",
                "show_button": False 
            }
        )
