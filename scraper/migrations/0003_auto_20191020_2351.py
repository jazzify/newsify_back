# Generated by Django 2.2.6 on 2019-10-20 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0002_auto_20191017_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='type',
            field=models.CharField(choices=[('ETP', 'ELTIEMPO'), ('EPS', 'ELPAIS'), ('NYT', 'NYT'), ('TWP', 'TWP')], max_length=3),
        ),
    ]
