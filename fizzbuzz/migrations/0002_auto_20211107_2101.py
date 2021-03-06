# Generated by Django 3.2.9 on 2021-11-07 21:01

from django.db import migrations
from django.utils import timezone



def create_sample_fizzbuzz_data(apps,schema_editor):
    fizzbuzz = apps.get_model('fizzbuzz','FizzBuzz')
    fizzbuzz (
        fizzbuzz_id = 1,
        message = 'Fizzbuzz 1',
        creation_date = timezone.now(),
        user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36'
    ).save()

    fizzbuzz (
        fizzbuzz_id = 2,
        message = 'Fizzbuzz 2',
        creation_date = timezone.now(),
        user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36'
    ).save()


class Migration(migrations.Migration):

    dependencies = [
        ('fizzbuzz', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_sample_fizzbuzz_data)
    ]



# from datetime import timedelta
# from django.db.migrations import operations
# from django.utils import timezone
# from django.db import migrations



# class Migration(migrations.Migration):
#     depencies = [
#         ('fizzbuzz','0001_initial')
#     ]

#     operations = [
#         migrations.RunPython(create_sample_fizzbuzz_data)
#     ]