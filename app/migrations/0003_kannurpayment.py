# Generated by Django 4.2.2 on 2024-01-29 04:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_enkollam_enkozhikode_knrregistraion_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='kannurpayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paymentdate', models.DateField(max_length=10)),
                ('paymentbalance', models.FloatField(max_length=100)),
                ('paymentamount', models.FloatField(max_length=100)),
                ('knrpaymentid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.knrregistraion')),
            ],
        ),
    ]
