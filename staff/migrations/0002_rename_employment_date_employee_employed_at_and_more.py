# Generated by Django 4.0.3 on 2022-03-16 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='employment_date',
            new_name='employed_at',
        ),
        migrations.AlterField(
            model_name='employee',
            name='chief',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='staff.employee'),
        ),
    ]
