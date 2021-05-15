# Generated by Django 3.1.7 on 2021-05-14 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0004_bankstatement'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bankstatement',
            name='sender',
        ),
        migrations.AddField(
            model_name='bankstatement',
            name='receiver_accno',
            field=models.CharField(default=True, max_length=10),
        ),
    ]
