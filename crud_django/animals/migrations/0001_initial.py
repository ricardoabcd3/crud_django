# Generated by Django 4.1 on 2022-08-30 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('species', models.CharField(max_length=200)),
                ('color', models.CharField(max_length=200)),
                ('extintion_warming', models.BooleanField()),
            ],
        ),
    ]
