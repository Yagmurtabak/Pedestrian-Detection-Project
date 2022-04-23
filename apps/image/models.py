import os

from django.db import models
from django.utils.translation import gettext_lazy as _
from config.models import CreationModificationDateBase


class ImageModel(CreationModificationDateBase):
    image = models.ImageField(_("image"), upload_to='images')

    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"

    def __str__(self):
        return str(os.path.split(self.image.path)[-1])



class Image(models.Model):
    Name = models.CharField(max_length=20)
    Image = models.FileField(null=False , blank=False)