# Generated by Django 4.2.2 on 2023-06-28 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0003_post_choices'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='choices',
        ),
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('P', 'Publish'), ('D', 'Draft')], default='D', max_length=10, null=True),
        ),
    ]
