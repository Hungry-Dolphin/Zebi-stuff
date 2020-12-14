# Generated by Django 3.1.1 on 2020-10-11 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_auto_20201007_2038'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={'verbose_name_plural': 'Comments'},
        ),
        migrations.RemoveField(
            model_name='comments',
            name='bumps',
        ),
        migrations.AddField(
            model_name='book',
            name='summary',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]