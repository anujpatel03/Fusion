# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-09-12 04:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('globals', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ambulance_request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_request', models.DateTimeField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('reason', models.CharField(max_length=50)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='globals.ExtraInfo')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.CharField(max_length=100, null=True)),
                ('complaint', models.CharField(max_length=100, null=True)),
                ('date', models.DateField(auto_now=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='globals.ExtraInfo')),
            ],
        ),
        migrations.CreateModel(
            name='Counter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
                ('fine', models.IntegerField(default=0)),
                ('doc_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_name', models.CharField(max_length=50)),
                ('doctor_phone', models.CharField(max_length=10)),
                ('specialization', models.CharField(max_length=100)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Expiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('supplier', models.CharField(max_length=50)),
                ('expiry_date', models.DateField()),
                ('returned', models.BooleanField(default=False)),
                ('return_date', models.DateField(blank=True, null=True)),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital_name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Hospital_admit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital_doctor', models.CharField(max_length=100)),
                ('admission_date', models.DateField()),
                ('discharge_date', models.DateField(blank=True, null=True)),
                ('reason', models.CharField(max_length=50)),
                ('doctor_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='health_center.Doctor')),
                ('hospital_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health_center.Hospital')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='globals.ExtraInfo')),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('days', models.IntegerField(default=0)),
                ('times', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Prescribed_medicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('days', models.IntegerField(default=0)),
                ('times', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('test', models.CharField(blank=True, max_length=200, null=True)),
                ('appointment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='health_center.Appointment')),
                ('doctor_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='health_center.Doctor')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='globals.ExtraInfo')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.IntegerField(choices=[(0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), (3, 'Thursday'), (4, 'Friday'), (5, 'Saturday'), (6, 'Sunday')])),
                ('from_time', models.TimeField(blank=True, null=True)),
                ('to_time', models.TimeField(blank=True, null=True)),
                ('room', models.IntegerField()),
                ('date', models.DateField(auto_now=True)),
                ('doctor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health_center.Doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicine_name', models.CharField(max_length=100)),
                ('quantity', models.IntegerField(default=0)),
                ('threshold', models.IntegerField(default=10)),
            ],
        ),
        migrations.AddField(
            model_name='prescribed_medicine',
            name='medicine_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health_center.Stock'),
        ),
        migrations.AddField(
            model_name='prescribed_medicine',
            name='prescription_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health_center.Prescription'),
        ),
        migrations.AddField(
            model_name='medicine',
            name='medicine_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health_center.Stock'),
        ),
        migrations.AddField(
            model_name='medicine',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='globals.ExtraInfo'),
        ),
        migrations.AddField(
            model_name='expiry',
            name='medicine_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health_center.Stock'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='doctor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health_center.Doctor'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='schedule',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='health_center.Schedule'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='globals.ExtraInfo'),
        ),
    ]
