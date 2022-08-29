# Generated by Django 3.2.8 on 2021-10-23 10:16

from django.db import migrations, models
import django.db.models.deletion
import dynamic_forms.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dyforms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('form_name', models.CharField(max_length=100)),
                ('form_number', models.BigIntegerField(blank=True, null=True)),
                ('form_id', models.BigIntegerField(blank=True, null=True)),
                ('form_time', models.DateTimeField(auto_now=True, null=True)),
                ('form', dynamic_forms.models.FormField()),
            ],
        ),
        migrations.CreateModel(
            name='FormResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response', dynamic_forms.models.ResponseField()),
                ('form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dyapp.dyforms')),
            ],
        ),
    ]