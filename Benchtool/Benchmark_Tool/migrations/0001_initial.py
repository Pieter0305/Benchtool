# Generated by Django 3.1.13 on 2021-10-05 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Userdata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150)),
                ('device', models.TextField(blank=True, null=True)),
                ('label', models.TextField(blank=True, null=True)),
                ('float64', models.TextField(blank=True, null=True)),
                ('int64', models.TextField(blank=True, null=True)),
                ('int32', models.TextField(blank=True, null=True)),
                ('int16', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
