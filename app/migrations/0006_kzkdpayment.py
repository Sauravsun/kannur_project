# Generated by Django 4.2.2 on 2024-02-01 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_kollamregistration_kzkdregistration_kozhikodeflups'),
    ]

    operations = [
        migrations.CreateModel(
            name='kzkdpayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paymentdate', models.DateField(max_length=10)),
                ('paymentbalance', models.FloatField(max_length=100)),
                ('paymentamount', models.FloatField(max_length=100)),
                ('mod_payment', models.CharField(max_length=200)),
                ('kzkdpaymentid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.kzkdregistration')),
            ],
        ),
    ]
