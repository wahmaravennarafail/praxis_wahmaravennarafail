# Generated by Django 3.2.8 on 2021-10-13 08:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='pesanan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jml_makanan', models.IntegerField()),
                ('jml_minuman', models.IntegerField()),
                ('makanan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.makanan')),
                ('minuman', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.minuman')),
            ],
        ),
    ]
