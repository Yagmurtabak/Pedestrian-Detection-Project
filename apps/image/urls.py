from django.urls import path
from django.contrib import admin

from . import views

from image.views import Imagelist_view, UploadImage_view,ImageDetail_view, external_view,home_view
from django.conf.urls.static import static
from django.conf import settings


app_name = "image"

urlpatterns = [
    path("DetectPedestrianYOLO", views.UploadImage.as_view(), name="upload_image_url"),
    path('admin/', admin.site.urls),
    path("", home_view),
    path('UploadImage' ,UploadImage_view),
    path('ResizedImage' , Imagelist_view),
    path('ImageDetail/<int:id>', ImageDetail_view),
    path('external', external_view),
]


urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)