from django import forms
from .models import Feedback
from email_templates.utils import send_templated_email


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback

    def save(self, commit=True):
        instance = super(FeedbackForm, self).save()
        send_templated_email('feedback', {
            'name': instance.name,
            'message': instance.message,
            'add_time': instance.add_time,
            'contact': instance.contact,
            'city': instance.city,
            'department': instance.department,
        })
        print({
            'name': instance.name,
            'message': instance.message,
            'add_time': instance.add_time
        })
        return instance
