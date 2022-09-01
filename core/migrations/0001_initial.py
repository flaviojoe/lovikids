# Generated by Django 4.1 on 2022-09-01 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Desire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='nome')),
                ('weight', models.IntegerField(verbose_name='peso')),
            ],
            options={
                'verbose_name': 'desejo',
                'verbose_name_plural': 'desejos',
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='nome')),
                ('level', models.IntegerField(verbose_name='nível')),
            ],
            options={
                'verbose_name': 'tarefa',
                'verbose_name_plural': 'tarefas',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
