# Generated by Django 3.1.7 on 2021-06-28 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noteapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='image',
            field=models.ImageField(default=1, upload_to='photo'),
            preserve_default=False,
        ),
    ]