#!../venv/bin/python3.10

from django.db import models
from django.urls import reverse

# CK Editor Utilities
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class Publication(models.Model):

    title = models.CharField(max_length=64)
    # body_description = models.TextField()
    body_description = RichTextUploadingField()
    # CKEditor handles the images
    # image_address = models.CharField(max_length=256, blank=True)
    publication_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("publication:publication-post", kwargs={"id": self.id} )