from django.views.generic import UpdateView, TemplateView, RedirectView
from .forms import ProfileForm
from .models import UserProfile
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import logout


class ProfileUpdate(UpdateView):
    form_class = ProfileForm
    template_name = 'personal/profile_edit.html'

    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        return super(ProfileUpdate, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('personal:profile')

    def get_object(self, queryset=None):
        user = self.request.user
        profile, created = UserProfile.objects.get_or_create(user=user)
        return profile


class ProfileDeleteView(TemplateView):
    template_name = 'personal/profile_delete.html'


class ProfileDelete(RedirectView):

    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        c_user = User.objects.get(username=request.user)
        c_user.is_active = False
        c_user.save()
        logout(request)
        return super(ProfileDelete, self).dispatch(request, *args, **kwargs)

    def get_redirect_url(self, *args, **kwargs):
        return '/'