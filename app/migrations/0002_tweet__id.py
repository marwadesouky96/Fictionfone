# Generated by Django 2.1.2 on 2018-10-13 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='_id',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]