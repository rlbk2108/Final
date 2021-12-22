from django.db import models

class Info(models.Model):
    info_title = models.CharField(max_length=100)
    info_image = models.ImageField(upload_to='media/')
    info_description = models.CharField(max_length=200)
    date_of_pub = models.DateTimeField(max_length=100)

    Info.objects.order_by('info_title')