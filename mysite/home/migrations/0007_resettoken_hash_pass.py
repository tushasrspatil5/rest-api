# Generated by Django 3.1.7 on 2022-04-27 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_resettoken'),
    ]

    operations = [
        migrations.AddField(
            model_name='resettoken',
            name='hash_pass',
            field=models.TextField(default=''),
        ),
    ]