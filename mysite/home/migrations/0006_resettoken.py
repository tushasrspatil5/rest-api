# Generated by Django 3.1.7 on 2022-04-27 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20220426_1342'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResetToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=255)),
                ('token', models.CharField(max_length=255)),
            ],
        ),
    ]
