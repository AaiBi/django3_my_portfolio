# Generated by Django 3.1.4 on 2021-01-25 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_language',
            field=models.CharField(blank=True, max_length=1),
        ),
    ]