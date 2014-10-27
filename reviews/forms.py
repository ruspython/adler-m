from django import forms
from .models import Review, Comment
from personal.models import UserProfile
from cuser.middleware import CuserMiddleware


class ReviewForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        user = CuserMiddleware.get_user()
        if not user.is_anonymous():
            try:
                self.fields['name'].initial = UserProfile.objects.get(user=user).get_full_name()
            except UserProfile.DoesNotExist:
                pass

    class Meta:
        model = Review
        fields = ['name', 'review']


class CommentForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        user = CuserMiddleware.get_user()
        if not user.is_anonymous():
            try:
                self.fields['name'].initial = UserProfile.objects.get(user=user).get_full_name()
            except UserProfile.DoesNotExist:
                pass

    class Meta:
        model = Comment
        fields = ['name', 'comment', 'review']
        widgets = {
            'review': forms.HiddenInput
        }