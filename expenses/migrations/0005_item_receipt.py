# Generated by Django 4.0.5 on 2022-07-08 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0004_person_party_receipt_party'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='receipt',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='expenses.receipt'),
            preserve_default=False,
        ),
    ]