from django.db import models
from django.urls import reverse

# Create your models here.

class Request(models.Model):

    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Declined', 'Declined'),
    )

    REQ_CHOICES = (
        ('PTO', 'Paid Time Off'),
        ('Sick Day', 'Sick Day'),
    )

    request_id = models.CharField(max_length=8)
    # Same as User's username
    employee_id = models.CharField(max_length=150)

    request_type = models.CharField(max_length=8, choices=REQ_CHOICES)
    request_status = models.CharField(max_length=8, choices=STATUS_CHOICES,\
                                      default='Pending')
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.employee_id} - {self.request_type}\
            {self.start_date} to {self.end_date}"

    def get_absolute_url(self):
        return reverse("request:view_request", kwargs={"id": self.id})

    class Meta:
        app_label = 'req_leave'