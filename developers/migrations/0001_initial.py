# Generated by Django 3.1.2 on 2020-10-22 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('common', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_experience', models.FloatField()),
                ('location', models.CharField(max_length=100)),
                ('annual_ctc', models.FloatField()),
                ('linked_in_profile', models.URLField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('designation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='common.designation')),
                ('employment_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='common.employmenttype')),
                ('tech_stack', models.ManyToManyField(default=None, to='common.TechStack')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
            options={
                'verbose_name': 'developer',
            },
        ),
    ]