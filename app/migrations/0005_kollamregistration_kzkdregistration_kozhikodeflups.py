# Generated by Django 4.2.2 on 2024-02-01 09:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_knrregistraion_knr_amountpaid_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='kollamregistration',
            fields=[
                ('stu_id', models.AutoField(default=2001, primary_key=True, serialize=False, unique=True)),
                ('ko_fname', models.CharField(max_length=300)),
                ('ko_lname', models.CharField(max_length=300)),
                ('ko_fathername', models.CharField(max_length=300)),
                ('ko_mothername', models.CharField(max_length=300)),
                ('ko_place', models.CharField(max_length=300)),
                ('ko_qualification', models.CharField(max_length=300)),
                ('ko_phone', models.CharField(max_length=15)),
                ('ko_course', models.CharField(max_length=300)),
                ('ko_coursefee', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='kzkdregistration',
            fields=[
                ('stu_id', models.AutoField(default=3001, primary_key=True, serialize=False, unique=True)),
                ('kz_fname', models.CharField(max_length=300)),
                ('kz_lname', models.CharField(max_length=300)),
                ('kz_fathername', models.CharField(max_length=300)),
                ('kz_mothername', models.CharField(max_length=300)),
                ('kz_place', models.CharField(max_length=300)),
                ('kz_qualification', models.CharField(max_length=300)),
                ('kz_phone', models.CharField(max_length=15)),
                ('kz_course', models.CharField(max_length=300)),
                ('kz_coursefee', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='kozhikodeflups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date1', models.DateField(max_length=15)),
                ('response1', models.CharField(max_length=200)),
                ('enkzkdfl', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.enkozhikode')),
            ],
        ),
    ]
