from django import forms
from .models import Faq
from email_templates.utils import send_templated_email


class FaqForm(forms.ModelForm):
    class Meta:
        model = Faq
        fields = ['name', 'question']

    def save(self, commit=True):
        instance = super(FaqForm, self).save()
        send_templated_email('faq', {
            'name': instance.name,
            'question': instance.question,
        })
        return instance