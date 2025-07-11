from django.template.loader import render_to_string
from django.conf import settings
from django.utils.html import strip_tags

import resend
import logging

logger = logging.getLogger(__name__)


class EmailService:

    def __init__(self):
        resend.api_key = settings.RESEND_API_KEY

    def send_email(self, to_email, subject, html_content, text_content=None):
        """ Function to send email using resend """
        try:
            if not text_content:
                text_content = strip_tags(html_content)

            params = {
                "from": settings.DEFAULT_FROM_EMAIL,
                "to": [to_email],
                "subject": subject,
                "html": html_content,
                "text": text_content
            }

            email = resend.Emails.send(params=params)
            print(f"Email enviado correctamente a {to_email}, id: {email.get('id')}")
            return True, email.get('id')
        except Exception as e:
            print(f"Hubo un error en el envio de correo {e}")
            return False, str(e)
    

    def send_verification_email(self, user, verification_token):
        """ Email de verification """
        verification_link = f"{settings.FRONTEND_URL}/verify-email?token={verification_token}"

        context = {
            'user': user,
            'verification_link': verification_link,
            'frontend_url': settings.FRONTEND_URL
        }

        html_content = render_to_string('emails/email_verification.html', context)
        subject = "Verifica tu email"

        return self.send_email(user.email, subject, html_content)