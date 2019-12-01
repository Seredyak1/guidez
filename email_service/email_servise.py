from jinja2 import Template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

from email_service.models import EmailTemplate


class SendEmail:
    def __init__(self, send_email, template, context):
        self.email = send_email
        self.template = template
        self.context = context
        self.body = self.get_body()

    def get_body(self):
        template_to_render = Template(self.template.body)
        html = template_to_render.render(self.context)
        return html

    def send(self):
        EmailMultiAlternatives(
            subject=self.template.title,
            body=self.body,
            from_email=settings.EMAIL_HOST_USER,
            to=self.email,).send()
        return True


def invation_email(user):
    template = EmailTemplate.objects.get(type='confirm_email')
    context = {"name": user.get_full_name()}
    print(context)
    mail = SendEmail([user.email], template, context).send()
    return mail
