from django import forms
from .models import Review, Comment


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'review']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'comment', 'review']
        widgets = {
            'review': forms.HiddenInput
        }