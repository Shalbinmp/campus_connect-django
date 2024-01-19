# Generated by Django 3.2.21 on 2024-01-17 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TimeSchedule',
            fields=[
                ('schedule_id', models.AutoField(primary_key=True, serialize=False)),
                ('time', models.TimeField()),
                ('date', models.DateField()),
            ],
            options={
                'db_table': 'time_schedule',
                'managed': False,
            },
        ),
    ]