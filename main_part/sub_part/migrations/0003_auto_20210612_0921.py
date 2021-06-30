# Generated by Django 3.2.3 on 2021-06-12 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0002_consig'),
    ]

    operations = [
        migrations.CreateModel(
            name='usert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_name', models.CharField(max_length=100)),
                ('user_name', models.CharField(max_length=100)),
                ('user_email', models.EmailField(max_length=254)),
                ('user_phone', models.IntegerField()),
                ('user_password', models.CharField(max_length=100)),
                ('user_cpassword', models.CharField(max_length=100)),
                ('user_img', models.ImageField(blank=True, null=True, upload_to='image/%Y/%m/%d')),
            ],
        ),
        migrations.AlterField(
            model_name='consig',
            name='consig_contact',
            field=models.IntegerField(),
        ),
    ]