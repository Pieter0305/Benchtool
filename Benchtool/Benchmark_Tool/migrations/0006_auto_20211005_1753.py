# Generated by Django 3.1.13 on 2021-10-05 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Benchmark_Tool', '0005_auto_20211005_1752'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='Benchmark_Tool.userdata'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='device',
            name='device',
            field=models.CharField(default=0, max_length=150),
            preserve_default=False,
        ),
    ]
