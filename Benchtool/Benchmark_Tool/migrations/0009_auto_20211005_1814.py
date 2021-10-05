# Generated by Django 3.1.13 on 2021-10-05 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Benchmark_Tool', '0008_device_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='arc',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userdata',
            name='cores',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userdata',
            name='device',
            field=models.CharField(default=0, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userdata',
            name='float64',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userdata',
            name='int16',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userdata',
            name='int32',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userdata',
            name='int64',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userdata',
            name='label',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userdata',
            name='pname',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userdata',
            name='width',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Device',
        ),
    ]