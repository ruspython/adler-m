from .models import EmailTemplate
from django.template import Context, Template
from django.core.mail.message import EmailMultiAlternatives
from django.utils.html import strip_tags


def send_templated_email(template_code, context):
    try:
        email_template = EmailTemplate.objects.get(slug=template_code)
    except EmailTemplate.DoesNotExist:
        return
    c = Context(context)
    t = Template(email_template.template)
    message_html = t.render(c)
    message_clean = strip_tags(message_html)
    sender = email_template.sender
    recipients = email_template.recipients.split(',')
    mail = EmailMultiAlternatives(email_template.subject,
                                  message_html,
                                  sender,
                                  recipients,
                                  headers={'Reply-To': sender}
                                  )
    if message_html != message_clean:
        mail.attach_alternative(message_html, 'text/html')
    mail.send(fail_silently=False)