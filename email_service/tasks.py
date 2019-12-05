from celery import shared_task


@shared_task()
def send_email(email, title, body, context):
    """Send email to email address by EmailSender class"""
    from .email_service import EmailSender
    EmailSender(send_email=[email], title=title, body=body, context=context).send()
