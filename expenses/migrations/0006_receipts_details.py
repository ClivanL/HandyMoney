# Generated by Django 4.0.5 on 2022-07-07 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0005_remove_receipts_receiptid'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipts',
            name='details',
            field=models.CharField(default='not entered', max_length=100),
        ),
    ]
