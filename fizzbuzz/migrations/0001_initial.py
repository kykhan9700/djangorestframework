# Generated by Django 3.2.9 on 2021-11-07 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FizzBuzz',
            fields=[
                ('fizzbuzz_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_agent', models.TextField()),
                ('creation_date', models.DateTimeField()),
                ('message', models.TextField()),
            ],
        ),
    ]
