# Generated by Django 4.0.4 on 2022-12-27 04:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Poryfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=30)),
                ('company_name', models.CharField(max_length=30)),
                ('rasm1', models.ImageField(upload_to='media')),
                ('rasm2', models.ImageField(blank=True, null=True, upload_to='media')),
                ('rasm3', models.ImageField(blank=True, null=True, upload_to='media')),
                ('vaqt', models.DateField()),
                ('link', models.CharField(max_length=100)),
                ('tur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myfiles.type')),
            ],
        ),
    ]
