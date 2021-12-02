# Generated by Django 3.2 on 2021-07-05 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField(max_length=100)),
                ('mobile', models.IntegerField(max_length=100)),
                ('address', models.CharField(max_length=1000)),
            ],
        ),
        migrations.DeleteModel(
            name='CandidateModel',
        ),
    ]