from django.db import models

# Used to keep track of absences
class Absence_Calendar(models.Model):

    employee_id = models.CharField(max_length=64)
    start_date = models.DateField()
    end_date = models.DateField()
    date = models.DateField(auto_now_add=True)
    absent_counter = models.IntegerField()

    def save(self, *args, **kwargs):
        # Check if it's a new instance or an update
        if not self.pk:
            # New instance, increment absent_counter for the date range
            existing_entries = Absence_Calendar.objects.filter(
                date__range=[self.start_date, self.end_date]
            )

            # This is for counting the absence volume for a given date
            # Note, this is not up for date range in total
            if existing_entries.exists():
                max_counter = existing_entries.aggregate(\
                    models.Max('absent_counter'))['absent_counter__max']
                self.absent_counter = max_counter + 1 if max_counter else 1
            else:
                self.absent_counter = 1
        else:
            # Existing instance, update absent_counter
            existing_entries = Absence_Calendar.objects.filter(
                date__range=[self.start_date, self.end_date]
            ).exclude(pk=self.pk)

            self.absent_counter = existing_entries.count() + 1

        super().save(*args, **kwargs)


#  Used to count whenever a publication is published by date :)
class Publication_Calendar(models.Model):

    date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=64)
    count_publications = models.IntegerField(default=0)


    def __str__(self):
        return f"{self.date} - {self.count_publications} Publications"


    def get_next_count(self):
        # Retrieve the latest Publication_Calendar instance
        latest_entry = Publication_Calendar.objects.latest('date')

        # Increment the count_publications value by 1
        return latest_entry.count_publications + 1 if latest_entry else 1


    # class Meta:
    #     ordering = ['-date']