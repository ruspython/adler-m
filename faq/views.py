from django.views.generic import ListView, CreateView
from .models import Faq
from .forms import FaqForm
from django.core.urlresolvers import reverse


class FaqListView(ListView):
    model = Faq
    context_object_name = 'questions'
    template_name = 'faq/faq_list.html'

    def get_template_names(self):
        request = self.request
        if request.is_ajax():
            return 'faq/faq_page.html'
        else:
            return 'faq/faq_list.html'

    def get_queryset(self):
        return super(FaqListView, self).get_queryset().exclude(answer='')


class FaqCreateView(CreateView):
    form_class = FaqForm
    template_name = 'faq/create_faq.html'

    def get_success_url(self):
        return reverse('faq:faq_add_success')
