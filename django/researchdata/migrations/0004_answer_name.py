# Generated by Django 3.1.12 on 2021-06-18 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('researchdata', '0003_auto_20201216_2238'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='name',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]