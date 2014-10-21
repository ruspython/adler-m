from modeltranslation.admin import TranslationAdmin
from django.conf import settings
import requests
import hashlib
import re


class TranslationTabMixin(TranslationAdmin):

    class Media:
        def __init__(self):
            pass

        js = (
            'modeltranslation/js/force_jquery.js',
            '/static/js/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


def send_sms(numbers, message='', sender=None):

    numbers = re.sub('[^\d^,]', '', numbers)

    if not sender:
        sender = settings.SMS_SENDER

    username = settings.SMS_USERNAME

    m = hashlib.md5()
    m.update(settings.SMS_PASSWORD)
    password = m.hexdigest()
    request_url = 'http://api.fastsms.pro/send.php?username=%s&password=%s&sender=%s&numbers=%s&message=%s' % (
        username,
        password,
        sender,
        numbers,
        message
    )
    r = requests.post(
        request_url,
    )