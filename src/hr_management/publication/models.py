from django.db import models
from django.urls import reverse

# Create your models here.

class Publication(models.Model):

    title = models.CharField(max_length=64)
    body_description = models.TextField()
    image_address = models.CharField(max_length=256)
    publication_date = models.DateTimeField(auto_now_add=True)



    # def get_absolute_url(self):
    #     return reverse("publication:publication")