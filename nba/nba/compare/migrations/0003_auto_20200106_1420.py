# Generated by Django 3.0.2 on 2020-01-06 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compare', '0002_auto_20200106_1333'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='City',
        ),
    ]
