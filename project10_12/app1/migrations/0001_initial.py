# Generated by Django 5.1.2 on 2024-12-10 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='App1Product',
            fields=[
                ('proid', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('prodname', models.CharField(max_length=20)),
                ('qty', models.IntegerField()),
                ('price', models.FloatField()),
            ],
        ),
    ]
