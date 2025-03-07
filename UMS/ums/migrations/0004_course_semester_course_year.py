# Generated by Django 5.1.5 on 2025-01-27 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ums', '0003_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='semester',
            field=models.IntegerField(choices=[(1, 'Semester 1'), (2, 'Semester 2')], default=None),
        ),
        migrations.AddField(
            model_name='course',
            name='year',
            field=models.IntegerField(choices=[(1, 'Year 1'), (2, 'Year 2'), (3, 'Year 3'), (4, 'Year 4')], default=None),
        ),
    ]
