# Generated by Django 4.2.1 on 2023-07-02 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0009_post_num_of_clicks'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.FileField(null=True, upload_to='category/images'),
        ),
    ]
