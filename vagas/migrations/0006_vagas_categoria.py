# Generated by Django 4.0.6 on 2022-08-01 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vagas', '0005_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='vagas',
            name='categoria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='vagas.categoria'),
        ),
    ]
