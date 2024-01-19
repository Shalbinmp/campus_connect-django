from django.db import models

# Create your models here.



class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    register_id = models.IntegerField(unique=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    # course_id = models.IntegerField()


    class Meta:
        managed = False
        db_table = 'student'
