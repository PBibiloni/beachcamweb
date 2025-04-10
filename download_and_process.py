# Run this script to download and process the data contained in the django models:

# Before importing django, configure it
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
import django
django.setup()

from datetime import timedelta

from django.conf import settings
from django.utils import timezone

from apps.prediction.models import Snapshot
from apps.webcam.models import WebCam

from predictions.classes.BayesianPredictor import BayesianPredictor

import ssl
ssl._create_default_https_context = ssl._create_unverified_context  # To download pytorch model

predictors = [BayesianPredictor()]


def main():
    for beachcam in WebCam.objects.order_by('-id').all():
        
        if not beachcam.available:
            continue

        snapshot = beachcam.create_snapshot()
        
        for predictor in predictors:
            try:
                predictionDTO = predictor.predict(snapshot.webcam_image.path)
                snapshot.predicted_crowd_count = predictionDTO.crowd_count
                prediction_image_path = beachcam.relative_filepath(timestamp=snapshot.ts, subfolder='img/predictions/', extension='.jpg')
                with open(os.path.join(settings.MEDIA_ROOT, prediction_image_path), 'wb') as f:
                    f.write(predictionDTO.img_predict_content)
                snapshot.predicted_image.name = prediction_image_path
                snapshot.save()
            except Exception as e:
                # Handle any exception
                print(f"download_and_process.py an error ocurred: {e}")
                raise e
                # TODO: make it NOT available.

        print(f"Downloaded and processed {beachcam.beach_name}.")
        
    # Delete the outdated images of the file system from outdated predictions
    for outdated_pred in Snapshot.objects.filter(ts__lte=timezone.now() - timedelta(days=1)):
        # TODO: Move `webcam_image` into a new storage server, rather than deleting it?
        if outdated_pred.webcam_image:
            outdated_pred.webcam_image.delete(save=True)
        if outdated_pred.webcam_video:
            outdated_pred.webcam_image.delete(save=True)
        if outdated_pred.predicted_image:
            outdated_pred.predicted_image.delete(save=True)


if __name__ == "__main__":
    main()
