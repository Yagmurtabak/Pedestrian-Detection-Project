from django import forms
from .models import ImageModel
from .models import Image


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = ['image']


class ImageForm(forms.ModelForm):

    class Meta:
        model = Image

        fields = [
           'Name', 'Image']