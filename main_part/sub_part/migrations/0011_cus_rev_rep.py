# Generated by Django 3.2.3 on 2021-06-30 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0010_rename_load_addr_load_entryt_load_addre'),
    ]

    operations = [
        migrations.CreateModel(
            name='cus_rev_rep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cus_name', models.CharField(max_length=100)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
            ],
        ),
    ]
