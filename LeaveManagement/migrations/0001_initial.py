# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-21 12:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LeaveApplication',
            fields=[
                ('leave_id', models.AutoField(primary_key=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('responded_on', models.DateTimeField(auto_now=True, null=True)),
                ('leave_type', models.CharField(choices=[('SL', 'SickLeave'), ('EL', 'EarnedLeave'), ('PL', 'PersonalLeave')], max_length=2)),
                ('number_of_days', models.IntegerField()),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('leave_status', models.CharField(choices=[('A', 'Approved'), ('R', 'Rejected')], default='R', max_length=1)),
                ('additional_message', models.TextField(max_length=200)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applicant', to=settings.AUTH_USER_MODEL)),
                ('approver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='approver', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'LeaveApplication',
            },
        ),
        migrations.CreateModel(
            name='LeaveRecordDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sick_leaves', models.IntegerField(default=14)),
                ('earned_leaves', models.IntegerField(default=14)),
                ('personal_leaves', models.IntegerField(default=14)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee', to=settings.AUTH_USER_MODEL)),
                ('reporting_manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reporting_manager', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'LeaveRecord',
            },
        ),
    ]
