# Generated by Django 2.2.7 on 2020-03-30 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20191205_0826'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='language',
            new_name='languages',
        ),
    ]
