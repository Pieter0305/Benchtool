# Generated by Django 3.1.13 on 2021-10-05 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Benchmark_Tool', '0003_auto_20211005_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='arc',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='cores',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='device',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='pname',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='width',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='username',
            field=models.TextField(blank=True, null=True),
        ),
    ]
