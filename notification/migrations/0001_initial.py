# Generated by Django 3.2.21 on 2024-01-17 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notifiction',
            fields=[
                ('notification_id', models.AutoField(primary_key=True, serialize=False)),
                ('notification', models.CharField(max_length=500)),
                ('time', models.TimeField()),
                ('date', models.DateField()),
            ],
            options={
                'db_table': 'notifiction',
                'managed': False,
            },
        ),
    ]
