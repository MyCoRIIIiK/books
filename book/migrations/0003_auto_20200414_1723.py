# Generated by Django 3.0.5 on 2020-04-14 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20200414_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='book.Reviews', verbose_name='Родитель'),
        ),
    ]
