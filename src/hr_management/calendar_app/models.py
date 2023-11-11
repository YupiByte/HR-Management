from django.db import models

# Don't Create your models here.

# Used to keep track of absences
class Absence_Calendar(models.Model):
    employee_id = models.CharField(max_length=64)
    absent_date_start = models.DateField()
    absent_date_end = models.DateField()
    date = models.DateField(auto_now_add=True)
    absent_counter = models.IntegerField()

    def save(self, *args, **kwargs):
        # Check if it's a new instance or an update
        if not self.pk:
            # New instance, increment absent_counter
            last_calendar_entry = \
                Absence_Calendar.objects.filter(\
                    employee_id=self.employee_id).order_by('-date').first()
            
            if last_calendar_entry:
                self.absent_counter = last_calendar_entry.absent_counter + 1
            else:
                self.absent_counter = 1

        super().save(*args, **kwargs)


#  Used to count whenever a publication is published by date :)
class Publication_Calendar(models.Model):

    date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=64)
    count_publications = models.IntegerField(default=1)


    def __str__(self):
        return f"{self.date} - {self.count_publications} Publications"


    def get_next_count(self):
        # Retrieve the latest Publication_Calendar instance
        latest_entry = Publication_Calendar.objects.latest('date')

        # Increment the count_publications value by 1
        return latest_entry.count_publications + 1 if latest_entry else 1


    # class Meta:
    #     ordering = ['-date']