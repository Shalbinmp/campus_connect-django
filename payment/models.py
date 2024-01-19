from django.db import models

# Create your models here.
from student.models import Student


class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    cvv = models.IntegerField()
    amount = models.IntegerField()
    card_number = models.IntegerField(db_column='card number')  # Field renamed to remove unsuitable characters.
    upi = models.CharField(max_length=50)
    net_banking = models.IntegerField(db_column='net banking')  # Field renamed to remove unsuitable characters.
    card_holder_name = models.CharField(db_column='card holder name', max_length=50)  # Field renamed to remove unsuitable characters.
    # student_id = models.IntegerField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'payment'
