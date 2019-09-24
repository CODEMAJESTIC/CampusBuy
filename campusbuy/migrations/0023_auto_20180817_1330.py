# Generated by Django 2.0.1 on 2018-08-17 12:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('campusbuy', '0022_remove_itemadvert_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemadvert',
            name='Created_date',
        ),
        migrations.AlterField(
            model_name='itemadvert',
            name='published_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
