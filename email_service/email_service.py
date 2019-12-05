from jinja2 import Template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

from .models import EmailTemplate
from .tasks import send_email


class EmailSender:
    """
    Render html template with context and send it in email.
    :param send_email: list, include email where SEND html data
    :param title: title of email
    :param body: html data with default variables
    :param context: dict, where key=body variable, value=some data in str, int, float
    """
    def __init__(self, send_email, title, body, context):
        self.email = send_email
        self.title = title
        self.body = body
        self.context = context
        self.body = self.get_body()

    def get_body(self):
        """Returnrender html data, include context values"""
        template_to_render = Template(self.body)
        html = template_to_render.render(self.context)
        return html

    def send(self):
        """Send by EmailMultiAlternatives class"""
        EmailMultiAlternatives(
            subject=self.title,
            body=self.body,
            from_email=settings.EMAIL_HOST_USER,
            to=self.email,).send()


def confirm_email(email, full_name):
    """Send confirm email about success registrations"""
    template = EmailTemplate.objects.get(type='confirm_email')
    context = {"name": full_name}
    mail = send_email.delay(email=email, title=template.title, body=template.body, context=context)
    return mail
