# Generated by Django 4.2.1 on 2023-07-05 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_rename_status_requirementassessment_work_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='requirementassessment',
            name='comment',
            field=models.TextField(blank=True, null=True, verbose_name='Comment'),
        ),
    ]