# Generated by Django 3.2.21 on 2024-01-17 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('course_id', models.AutoField(primary_key=True, serialize=False)),
                ('course', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'courses',
                'managed': False,
            },
        ),
    ]