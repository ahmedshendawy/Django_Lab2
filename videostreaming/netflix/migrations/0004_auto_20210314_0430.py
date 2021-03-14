# Generated by Django 3.1.7 on 2021-03-14 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netflix', '0003_auto_20210314_0407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='poster',
            field=models.ImageField(upload_to='videostreaming/posters'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='video',
            field=models.FileField(upload_to='videostreaming/videos'),
        ),
    ]