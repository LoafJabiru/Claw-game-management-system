# Generated by Django 5.1.1 on 2024-11-30 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GameApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prize_id', models.CharField(max_length=100)),
                ('prize_name', models.CharField(max_length=100)),
                ('value', models.IntegerField()),
            ],
        ),
    ]
