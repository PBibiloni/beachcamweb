from django.shortcuts import render

from data.models import BeachCam
from django.shortcuts import get_object_or_404, render


# Create your views here.


def home(request):
    """ Returns home page. """
    beachcams = list(BeachCam.objects.all())
    return render(request, 'core/home.html', context={'cams': beachcams})


def show_image(request, beach_name):
    """ Returns ajax_image of latest prediction overimposed on captured image. """
    beachcam = get_object_or_404(BeachCam, beach_name=beach_name)
    other_beachcams = BeachCam.objects.exclude(beach_name=beach_name)
    return render(request, 'core/show_image.html', context={'cam': beachcam, 'other_cams': other_beachcams, 'prediction': beachcam.last_prediction})

def show_analyze_image(request):
    return render(request, 'core/analyze_image.html')
