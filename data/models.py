from django.db import models


class BeachCam(models.Model):
    beach_name = models.CharField(max_length=200, unique=True)
    beach_latitude = models.DecimalField(max_digits=9, decimal_places=6)
    beach_longitude = models.DecimalField(max_digits=9, decimal_places=6)
    url_image = models.CharField(max_length=200)
    url_aemet = models.CharField(max_length=200, null=True, blank=True)
    url_platgesbalears = models.CharField(max_length=200, null=True, blank=True)
    probe_freq_mins = models.IntegerField(default=60)

    max_crowd_count = models.IntegerField()

    def __str__(self):
        return self.beach_name

    def last_prediction(self):
        return self.prediction_set.order_by('-ts').first()


class Prediction(models.Model):
    beachcam = models.ForeignKey(BeachCam, on_delete=models.CASCADE)
    ts = models.DateTimeField()
    image = models.ImageField(null=True, upload_to='count/')
    crowd_count = models.FloatField(default=0)

    def __str__(self):
        return f'{self.beachcam.beach_name} - {self.ts}'
