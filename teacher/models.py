from django.db import models

# Create your models here.


class Teacher(models.Model):
    teacher_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=30)
    department = models.CharField(max_length=60)
    mobile_number = models.IntegerField(db_column='mobile number')  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'teacher'
