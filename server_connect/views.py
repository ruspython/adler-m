from django.views.generic import TemplateView, View
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib.auth import authenticate
from catalog.xml_import import data_import


class ImportRequest(TemplateView):
    template_name = 'server_connect/request.html'

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(ImportRequest, self).dispatch(request, *args, **kwargs)

    @staticmethod
    def post(request, *args, **kwargs):
        post_data = request.POST
        user = authenticate(username=post_data.get('login', None), password=post_data.get('password', None))
        if user:
            data = post_data.get('xml', None)
            data_import(data)
            return HttpResponse('ok')
        else:
            return HttpResponse(status=403)

    def get_context_data(self, **kwargs):
        context = super(ImportRequest, self).get_context_data(**kwargs)
        context['method'] = 'get'
        return context