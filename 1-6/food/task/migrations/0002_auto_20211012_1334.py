# Generated by Django 3.2.8 on 2021-10-12 06:34

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='minuman',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jenis', models.CharField(max_length=200)),
                ('nama', models.CharField(max_length=200)),
                ('harga', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='makanan',
            name='jenis_makanan',
        ),
        migrations.RemoveField(
            model_name='makanan',
            name='jml',
        ),
        migrations.RemoveField(
            model_name='makanan',
            name='nama_makanan',
        ),
        migrations.AddField(
            model_name='makanan',
            name='jenis',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='makanan',
            name='nama',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='pesanan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Jumlah_makanan', models.IntegerField()),
                ('jumlah_minuman', models.IntegerField()),
                ('jenis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.makanan')),
                ('minuman', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.minuman')),
            ],
        ),
    ]
