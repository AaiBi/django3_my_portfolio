# Generated by Django 3.1.4 on 2021-01-25 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_project_project_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='css',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='project',
            name='django',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='project',
            name='html',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='project',
            name='javascript',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='project',
            name='python',
            field=models.BooleanField(default=False),
        ),
    ]