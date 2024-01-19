from django.db import models

# Create your models here.

class Notifiction(models.Model):
    notification_id = models.AutoField(primary_key=True)
    notification = models.CharField(max_length=500)
    time = models.TimeField()
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'notifiction'
