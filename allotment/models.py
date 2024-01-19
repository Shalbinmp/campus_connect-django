from django.db import models

# Create your models here.

class Allotment(models.Model):
    allotment_id = models.AutoField(primary_key=True)
    cap_id = models.CharField(unique=True, max_length=30)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    dob = models.DateField(db_column='DOB')  # Field name made lowercase.
    address = models.CharField(max_length=300)
    mobile_number = models.CharField(db_column='mobile number', max_length=11)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'allotment'
