from django.db import models
from student.models import Student

# Create your models here.


class Compliant(models.Model):
    compliant_id = models.AutoField(primary_key=True)
    complaint = models.CharField(max_length=500)
    date = models.DateField()
    time = models.TimeField()
    student_id = models.IntegerField()
    # student = models.ForeignKey(Student,to_field='student_id', on_delete=models.CASCADE)
    reply = models.CharField(max_length=42)

    class Meta:
        managed = False
        db_table = 'compliant'
