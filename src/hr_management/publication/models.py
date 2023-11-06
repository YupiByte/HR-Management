#!../venv/bin/python3.10

from django.db import models
from django.urls import reverse

# CK Editor Utilities
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


# Models the Publication Editor to present to the Admin
class Publication(models.Model):

    title = models.CharField(max_length=64)

    # CKEditor Class handles the images, their locations
    # and can even store them in the server,
    # allowing for the administrator to utilize them without
    # reuploading images
    body_description = RichTextUploadingField()

    # image_address may be obsolete given the above functionality
    # image_address = models.CharField(max_length=256, blank=True)

    # Generates the date at moment of post
    publication_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("publication:publication-post", kwargs={"id": self.id} )