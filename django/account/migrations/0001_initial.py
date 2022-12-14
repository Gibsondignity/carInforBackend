# Generated by Django 3.1.7 on 2022-11-26 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_number', models.CharField(max_length=50)),
                ('owner_name', models.CharField(max_length=50)),
                ('picture', models.FileField(upload_to='media/')),
                ('owner_dob', models.DateField()),
                ('car_model', models.CharField(max_length=50)),
                ('car_type', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=50)),
                ('date_of_reg', models.DateTimeField()),
                ('region_of_reg', models.CharField(max_length=50)),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('date_updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
