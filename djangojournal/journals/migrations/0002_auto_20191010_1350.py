# Generated by Django 2.2.6 on 2019-10-10 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='journal_entry',
            field=models.TextField(max_length=10000),
        ),
    ]