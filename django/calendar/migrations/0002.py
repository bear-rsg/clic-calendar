from django.db import migrations
from calendar import models


def insert_years(apps, schema_editor):
    """
    Inserts year objects for each year the project will run
    """

    years = [2020, 2021, 2022, 2023, 2024, 2025]

    for year in years:
        models.Year(name=year).save()


def insert_months(apps, schema_editor):
    """
    Inserts months objects for each month of the year
    """

    months = [
        {"name": "January", "name_short": "Jan", "number": 1},
        {"name": "February", "name_short": "Feb", "number": 2},
        {"name": "March", "name_short": "Mar", "number": 3},
        {"name": "April", "name_short": "Apr", "number": 4},
        {"name": "May", "name_short": "May", "number": 5},
        {"name": "June", "name_short": "Jun", "number": 6},
        {"name": "July", "name_short": "Jul", "number": 7},
        {"name": "August", "name_short": "Aug", "number": 8},
        {"name": "September", "name_short": "Sep", "number": 9},
        {"name": "October", "name_short": "Oct", "number": 10},
        {"name": "November", "name_short": "Nov", "number": 11},
        {"name": "December", "name_short": "Dec", "number": 12},
    ]

    for month in months:
        models.Month(
            name=month["name"],
            name_short=month["name_short"],
            number=month["number"]
            ).save()


class Migration(migrations.Migration):

    dependencies = [
        ('calendar', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(insert_years),
        migrations.RunPython(insert_months),
    ]
