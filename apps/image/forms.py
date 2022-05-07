from django import forms
from .models import ImageModel,PedestrianDetectSSD
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


class PedestrianDetectSSDForm(forms.ModelForm):
    class Meta:
        model = PedestrianDetectSSD
        fields = ['image']