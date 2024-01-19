from django.db import models

# Create your models here.

class Feedback(models.Model):
    feedback_id = models.AutoField(primary_key=True)
    feedback = models.CharField(max_length=500)
    date = models.DateField()
    time = models.TimeField()
    student_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'feedback'
