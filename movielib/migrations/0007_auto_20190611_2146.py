# Generated by Django 2.1.2 on 2019-06-11 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movielib', '0006_auto_20190611_2139'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='Modified_Date',
            new_name='ModifiedD',
        ),
    ]
