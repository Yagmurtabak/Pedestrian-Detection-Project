
from django.shortcuts import render

from apps.image.object_detection import object_detection

from .forms import ImageForm
from .models import Image
from subprocess import run,PIPE
import sys
import cv2
import numpy as np
import os

import io
from PIL import Image as im
import torch
from image.object_detection import object_detection

from django.shortcuts import render
from django.views.generic.edit import CreateView

from .models import ImageModel, PedestrianDetectSSD
from .forms import ImageUploadForm, PedestrianDetectSSDForm
from image.models import Detector

class UploadImageSSD(CreateView):
    model = PedestrianDetectSSD
    template_name = 'image/ssd.html'
    fields = ["image"] 

        
    def post(self,request , *args, **kwargs):

    

        form = PedestrianDetectSSDForm(request.POST, request.FILES)
        if form.is_valid():
            img = request.FILES.get('image')
            img_instance = PedestrianDetectSSD(
                image=img
            )
            img_instance.save()

            uploaded_img_qs = PedestrianDetectSSD.objects.filter().last()
            img_bytes = uploaded_img_qs.image.read()
            img = im.open(io.BytesIO(img_bytes)).convert('RGB') 
            open_cv_image = np.array(img) 
            # Convert RGB to BGR 
            open_cv_image = open_cv_image[:, :, ::-1].copy()
        
            model = object_detection()
 
            results = model.detect(open_cv_image)
            cv2.imwrite('media/ssd_out/image0.jpg', results[0])

        inference_img = "/media/ssd_out/image0.jpg"

        form = PedestrianDetectSSDForm()
        context = {
            "form": form,
            "inference_img": inference_img
        }
        return render(request, 'image/ssd.html', context)

    

class UploadImage(CreateView):
    model = ImageModel
    template_name = 'image/imagemodel_form.html'
    fields = ["image"]

    def post(self,request , *args, **kwargs):
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            img = request.FILES.get('image')
            img_instance = ImageModel(
                image=img
            )
            img_instance.save()

            uploaded_img_qs = ImageModel.objects.filter().last()
            img_bytes = uploaded_img_qs.image.read()
            img = im.open(io.BytesIO(img_bytes))

            path_hubconfig = "C:/Users/Yagmur/OneDrive/Masaüstü/Pedestrian-Detection-Project/yolov5"
            path_weightfile = "C:/Users/Yagmur/OneDrive/Masaüstü/Pedestrian-Detection-Project/yolov5_code/yolov5s.pt"  # or any custom trained model

            model = torch.hub.load(path_hubconfig, 'custom',
                                   path=path_weightfile, source='local')
            

            results = model(img, size=640)
            results.render()
            for img in results.imgs:
                img_base64 = im.fromarray(img)
                img_base64.save("media/yolo_out/image0.jpg", format="JPEG")

            inference_img = "/media/yolo_out/image0.jpg"

            form = ImageUploadForm()
            context = {
                "form": form,
                "inference_img": inference_img
            }
            return render(request, 'image/imagemodel_form.html', context)

        else:
            form = ImageUploadForm()
        context = {
            "form": form
        }
        return render(request, 'image/imagemodel_form.html', context)




def UploadImage_view(request):   
    form = ImageForm(request.POST, request.FILES ) 
    


    if form.is_valid():
        form.save()

            
    context = {
        'form': form,
    }

    return render(request, 'form.html', context)

def ResizedImage_view(request):
    sayfa = "Resized Image"
    return render(request, "page.html", {"sayfa": sayfa})


def Imagelist_view(request):
    Images = Image.objects.all()

    return render(request , "Resized.html",{"Images": Images})

def ImageDetail_view(request, id):
    Images = Image.objects.get(id=id)
    return render(request , "detail.html", {"Image": Images})


def external_view(request):
    inp=request.POST.get('Image')
    out= run([sys.executable,'C://Users//Yagmur//OneDrive//Masaüstü//Pedestrian-Detection-Project//resized.py'],inp,shell=False,stdout=PIPE)
    print(out)
    return render(request,'external.html',{'data1':out.stdout})


def home_view(request):
    sayfa = "Ana Sayfa"
    return render(request, "page.html", {"sayfa": sayfa})