# Generated by Django 3.0.5 on 2020-05-03 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='wikiEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search', models.CharField(max_length=50)),
                ('search_date', models.DateTimeField()),
                ('ip_address', models.CharField(max_length=39)),
            ],
        ),
    ]
