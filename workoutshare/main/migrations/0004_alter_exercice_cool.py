# Generated by Django 4.1.6 on 2023-02-15 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_musclegroup_name_alter_program_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercice',
            name='cool',
            field=models.DurationField(default=180, max_length=1000),
        ),
    ]
