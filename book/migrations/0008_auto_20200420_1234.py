# Generated by Django 3.0.5 on 2020-04-20 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0007_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='book',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='star',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.DeleteModel(
            name='Rating',
        ),
        migrations.DeleteModel(
            name='RatingStar',
        ),
    ]
