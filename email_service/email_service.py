from django.template import Template, Context
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

from .models import EmailTemplate
from .tasks import send_email


class EmailSender:
    """
    Render html template with context and send it in email.
    :param to: list, include email where SEND html data
    :param title: title of email
    :param body: html data with default variables
    :param context: dict, where key=body variable, value=some data in str, int, float
    """
    def __init__(self, send_emails, title, body, context):
        self.to = [send_emails]
        self.title = title
        self.tbody = body
        self.context = context
        self.body = self.get_body()

    def get_body(self):
        """Return render html data, include context values"""
        context = Context(self.context)
        html_message = Template(self.tbody)
        html = html_message.render(context)
        return html

    def send(self):
        """Send by EmailMultiAlternatives class"""
        msg = EmailMultiAlternatives(
            subject=self.title,
            body=self.body,
            from_email=settings.EMAIL_HOST_USER,
            to=self.to,
            alternatives=((self.body, 'text/html'),),)
        msg.send()


def confirm_email(email, full_name):
    """Send confirm email about success registrations"""
    template = EmailTemplate.objects.get(type='confirm_email')
    context = {"name": full_name}
    mail = send_email.delay(email=email, title=template.title, body=template.body, context=context)
    return mail
