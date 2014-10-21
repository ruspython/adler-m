from django import forms
from .models import UploadedCollectionItem
from .widgets import PreviewImageWidget


class UploadCollectionItemForm(forms.ModelForm):

    class Meta:
        model = UploadedCollectionItem
        fields = ['image', 'name', 'manufacturer', 'scale']
        widgets = {'image': PreviewImageWidget()}