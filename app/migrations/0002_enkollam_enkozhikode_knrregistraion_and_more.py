# Generated by Django 4.2.2 on 2024-01-28 09:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='enkollam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=300)),
                ('lname', models.CharField(max_length=300)),
                ('place', models.CharField(max_length=300)),
                ('qualification', models.CharField(max_length=300)),
                ('phone', models.CharField(max_length=15)),
                ('course', models.CharField(max_length=300)),
                ('date', models.DateField(max_length=300)),
                ('staus', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='enkozhikode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=300)),
                ('lname', models.CharField(max_length=300)),
                ('place', models.CharField(max_length=300)),
                ('qualification', models.CharField(max_length=300)),
                ('phone', models.CharField(max_length=15)),
                ('course', models.CharField(max_length=300)),
                ('date', models.DateField(max_length=300)),
                ('staus', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='knrregistraion',
            fields=[
                ('stu_id', models.AutoField(default=1001, primary_key=True, serialize=False, unique=True)),
                ('knr_fname', models.CharField(max_length=300)),
                ('knr_lname', models.CharField(max_length=300)),
                ('knr_fathername', models.CharField(max_length=300)),
                ('knr_mothername', models.CharField(max_length=300)),
                ('knr_place', models.CharField(max_length=300)),
                ('knr_qualification', models.CharField(max_length=300)),
                ('knr_phone', models.CharField(max_length=15)),
                ('knr_course', models.CharField(max_length=300)),
                ('knr_coursefee', models.CharField(max_length=300)),
                ('knr_amountpaid', models.CharField(max_length=300)),
                ('knr_dop', models.CharField(max_length=15)),
                ('knr_mod', models.CharField(max_length=300)),
            ],
        ),
        migrations.AlterField(
            model_name='enkannur',
            name='date',
            field=models.DateField(max_length=8),
        ),
        migrations.AlterField(
            model_name='enkannur',
            name='phone',
            field=models.CharField(max_length=15),
        ),
        migrations.CreateModel(
            name='kollmflups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date1', models.DateField(max_length=15)),
                ('response1', models.CharField(max_length=200)),
                ('enkollmfl', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.enkollam')),
            ],
        ),
        migrations.CreateModel(
            name='knrflups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date1', models.DateField(max_length=15)),
                ('response1', models.CharField(max_length=200)),
                ('enkannurfl', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.enkannur')),
            ],
        ),
    ]
