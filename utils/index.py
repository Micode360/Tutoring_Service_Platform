def send_smtp_mail(subject, from_email, to, render_to_string, EmailMultiAlternatives, **kwargs):

    # Render HTML template
    html_content = render_to_string("message.html",kwargs)
    text_content = "Welcome to our app!"

    # Create email
    msg = EmailMultiAlternatives(subject, text_content, from_email, to)
    msg.attach_alternative(html_content, "text/html")
    msg.send()