# Generated by Django 3.2.3 on 2021-06-23 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0006_dispatcht'),
    ]

    operations = [
        migrations.CreateModel(
            name='drivert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('did', models.CharField(max_length=100)),
                ('ddob', models.DateField()),
                ('dfname', models.CharField(max_length=100)),
                ('dlname', models.CharField(max_length=100)),
                ('daddr', models.CharField(max_length=200)),
                ('dcity', models.CharField(max_length=100)),
                ('dstate', models.CharField(max_length=100)),
                ('dzip', models.IntegerField()),
                ('dssn', models.CharField(max_length=100)),
                ('dphone', models.IntegerField()),
                ('demail', models.EmailField(max_length=254)),
                ('dins', models.IntegerField()),
                ('dins1', models.IntegerField()),
                ('difta', models.IntegerField()),
                ('dah', models.CharField(max_length=100)),
                ('dlicnum', models.CharField(max_length=100)),
                ('dlicexp', models.CharField(max_length=100)),
                ('dmeddate', models.CharField(max_length=100)),
                ('dmedexp', models.CharField(max_length=100)),
                ('ddtest', models.CharField(max_length=100)),
                ('dpt', models.CharField(max_length=100)),
                ('dpm', models.CharField(max_length=100)),
                ('dem', models.CharField(max_length=100)),
                ('dper', models.IntegerField()),
                ('dstat', models.CharField(max_length=100)),
                ('dpp', models.IntegerField()),
                ('dlb', models.IntegerField()),
                ('dtrent', models.IntegerField()),
                ('dnote', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='shippert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ship_id', models.IntegerField()),
                ('ship_name', models.CharField(max_length=100)),
                ('cus_addr', models.CharField(max_length=100)),
                ('ship_city', models.CharField(max_length=100)),
                ('ship_state', models.CharField(max_length=100)),
                ('ship_country', models.CharField(max_length=100)),
                ('ship_zip', models.IntegerField()),
                ('ship_phone', models.IntegerField()),
                ('ship_email', models.EmailField(max_length=254)),
                ('ship_ext', models.CharField(max_length=100)),
                ('ship_contact', models.IntegerField()),
                ('ship_notes', models.CharField(max_length=100)),
            ],
        ),
    ]
