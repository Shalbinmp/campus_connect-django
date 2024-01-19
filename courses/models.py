from django.db import models

# Create your models here.
class Courses(models.Model):
    course_id = models.AutoField(primary_key=True)
    course = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'courses'
