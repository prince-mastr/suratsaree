# Generated by Django 2.2.4 on 2020-11-06 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_auto_20201106_0556'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='per_piece',
            field=models.FloatField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderitem',
            name='total_priece',
            field=models.FloatField(blank=True, default=0),
            preserve_default=False,
        ),
    ]
