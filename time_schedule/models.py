from django.db import models

# Create your models here.


class TimeSchedule(models.Model):
    schedule_id = models.AutoField(primary_key=True)
    time = models.TimeField()
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'time_schedule'
