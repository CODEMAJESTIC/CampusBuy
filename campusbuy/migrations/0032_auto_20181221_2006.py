# Generated by Django 2.0.1 on 2018-12-21 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campusbuy', '0031_advert_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='advert',
            options={'ordering': ['-published_date']},
        ),
        migrations.AlterField(
            model_name='category',
            name='Name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
