from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

def send_smtp_mail(subject, from_email, to, context):

    # Render HTML template
    html_content = render_to_string("message.html",context)
    text_content = "Welcome to our app!"

    # Create email
    msg = EmailMultiAlternatives(subject, text_content, from_email, to)
    msg.attach_alternative(html_content, "text/html")
    msg.send()