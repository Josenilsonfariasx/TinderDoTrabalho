# Generated by Django 4.0.6 on 2022-08-01 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vagas', '0003_alter_vagas_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='vagas',
            name='escolaridade',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
