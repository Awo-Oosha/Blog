# Generated by Django 4.2.2 on 2023-06-27 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default=None, null=True, upload_to='images/post'),
        ),
    ]
