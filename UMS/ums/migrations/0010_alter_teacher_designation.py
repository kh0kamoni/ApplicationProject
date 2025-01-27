# Generated by Django 5.1.5 on 2025-01-27 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ums', '0009_alter_teacher_designation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='designation',
            field=models.IntegerField(choices=[(1, 'Lectuerer'), (2, 'Assistant Professor'), (3, 'Associate Professor'), (4, 'Professor')], default=1),
        ),
    ]
