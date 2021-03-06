# Generated by Django 2.2.4 on 2020-08-30 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_sharelist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sharelist',
            name='slug',
            field=models.SlugField(default='12345678', max_length=8, unique=True),
        ),
        migrations.AlterField(
            model_name='sharelist',
            name='url',
            field=models.URLField(),
        ),
    ]
