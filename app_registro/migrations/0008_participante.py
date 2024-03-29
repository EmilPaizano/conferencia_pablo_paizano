# Generated by Django 3.2.3 on 2021-06-11 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_registro', '0007_alter_conferencista_nombre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25)),
                ('apellido', models.CharField(max_length=25)),
                ('correo', models.EmailField(max_length=254)),
                ('twitter', models.CharField(blank=True, max_length=35, null=True)),
            ],
        ),
    ]
