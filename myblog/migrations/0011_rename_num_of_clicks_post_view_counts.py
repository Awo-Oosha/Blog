# Generated by Django 4.2.1 on 2023-07-04 05:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0010_category_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='num_of_clicks',
            new_name='view_counts',
        ),
    ]
