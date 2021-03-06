# Generated by Django 3.2.3 on 2021-06-30 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0008_rename_cus_addr_shippert_ship_addr'),
    ]

    operations = [
        migrations.CreateModel(
            name='equipmentst',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('own_fname', models.CharField(max_length=100)),
                ('own_lname', models.CharField(max_length=100)),
                ('unit_no', models.CharField(max_length=100)),
                ('make', models.CharField(max_length=100)),
                ('eq_type', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('VIN', models.CharField(max_length=100)),
                ('p_no', models.CharField(max_length=100)),
                ('p_exp', models.DateField()),
                ('mileage', models.CharField(max_length=100)),
                ('truck', models.CharField(max_length=100)),
                ('trailer', models.CharField(max_length=100)),
                ('province', models.CharField(max_length=100)),
                ('axels', models.CharField(max_length=100)),
                ('fuel_type', models.CharField(max_length=100)),
                ('weight', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('deactive_date', models.DateField()),
                ('doti_date', models.DateField()),
                ('ifta_truck', models.CharField(max_length=100)),
                ('ai_date', models.DateField()),
                ('ndi_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='load_entryt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('load_id', models.CharField(max_length=100)),
                ('cus_name', models.CharField(max_length=100)),
                ('cus_load', models.CharField(max_length=100)),
                ('load_type', models.CharField(max_length=100)),
                ('load_date', models.DateField()),
                ('pickupdate', models.DateField()),
                ('deliverydate', models.DateField()),
                ('load_dispatch', models.CharField(max_length=100)),
                ('lh_rate', models.IntegerField()),
                ('unloading', models.IntegerField()),
                ('reimburse', models.CharField(max_length=10)),
                ('detention', models.IntegerField()),
                ('layover', models.IntegerField()),
                ('other_c', models.IntegerField()),
                ('total_c', models.IntegerField()),
                ('load_driver', models.CharField(max_length=100)),
                ('truck', models.CharField(max_length=100)),
                ('trailer', models.CharField(max_length=100)),
                ('rate', models.CharField(max_length=100)),
                ('load_shipper', models.CharField(max_length=100)),
                ('load_addr', models.CharField(max_length=200)),
                ('load_city', models.CharField(max_length=100)),
                ('load_state', models.CharField(max_length=100)),
                ('load_country', models.CharField(max_length=100)),
                ('load_zip', models.IntegerField()),
                ('load_weight', models.CharField(max_length=100)),
                ('load_qty', models.CharField(max_length=100)),
                ('ship_con', models.IntegerField()),
                ('load_note', models.CharField(max_length=200)),
                ('cons_name', models.CharField(max_length=100)),
                ('con_con', models.IntegerField()),
                ('con_addr', models.CharField(max_length=200)),
                ('con_city', models.CharField(max_length=100)),
                ('con_state', models.CharField(max_length=100)),
                ('con_country', models.CharField(max_length=100)),
                ('cons_zip', models.IntegerField()),
            ],
        ),
    ]
