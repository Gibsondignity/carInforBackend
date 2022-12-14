# Generated by Django 3.1.7 on 2022-12-12 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='reportedCar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reported_issue', models.CharField(max_length=50)),
                ('reported_date', models.DateTimeField(auto_now=True)),
                ('date_updated', models.DateTimeField(auto_now_add=True)),
                ('car_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.carinfo')),
            ],
        ),
    ]
