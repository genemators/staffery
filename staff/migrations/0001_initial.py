# Generated by Django 4.0.3 on 2022-03-13 18:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('position', models.CharField(max_length=255)),
                ('employment_date', models.DateTimeField()),
                ('chief', models.ForeignKey(default='root', on_delete=django.db.models.deletion.CASCADE, to='staff.employee')),
            ],
        ),
    ]
