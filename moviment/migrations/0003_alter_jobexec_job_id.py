# Generated by Django 4.1 on 2022-10-04 01:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        ('moviment', '0002_alter_jobexec_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobexec',
            name='job_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='job_name', to='core.job'),
            preserve_default=False,
        ),
    ]
