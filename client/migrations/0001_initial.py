# Generated by Django 4.0.3 on 2022-04-05 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resque',
            fields=[
                ('id', models.CharField(max_length=21, primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=200)),
                ('breed', models.CharField(max_length=20)),
                ('vaccination', models.CharField(default='no', max_length=3)),
                ('reason', models.CharField(max_length=100, null=True)),
                ('condition', models.CharField(default='Good', max_length=10)),
                ('date', models.CharField(max_length=19)),
                ('status', models.CharField(max_length=20)),
            ],
        ),
    ]
