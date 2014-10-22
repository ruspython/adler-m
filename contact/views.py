from django.views.generic import CreateView
from .models import *
from .forms import FeedbackForm
from django.core.urlresolvers import reverse


class CreateFeedbackView(CreateView):
    model = Feedback
    form_class = FeedbackForm
    template_name = 'contact/contact.html'

    def get_success_url(self):
        return reverse('contact:home')

    def get_context_data(self, **kwargs):
        context = super(CreateFeedbackView, self).get_context_data(**kwargs)
        context['no_map'] = Contact.objects.filter(use_map=False)
        context['with_map'] = Contact.objects.filter(use_map=True)
        return context