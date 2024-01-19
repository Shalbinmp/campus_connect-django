from django.db import models

# Create your models here.




class Forms(models.Model):
    forms_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=45)
    admin_form = models.CharField(max_length=350)
    submited_form = models.CharField(max_length=305)

    class Meta:
        managed = False
        db_table = 'forms'

