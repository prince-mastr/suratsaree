# Generated by Django 2.2.4 on 2020-09-02 17:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20200830_0324'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='owner',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='sharelist',
            name='share',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Share'),
        ),
    ]
