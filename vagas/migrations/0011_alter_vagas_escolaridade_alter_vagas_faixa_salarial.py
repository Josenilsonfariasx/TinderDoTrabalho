# Generated by Django 4.1 on 2022-08-09 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vagas', '0010_remove_vagas_categoria_alter_vagas_faixa_salarial_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vagas',
            name='escolaridade',
            field=models.CharField(choices=[('Ensino fundamental', 'Ensino Fundamental'), ('Ensino Medio', 'Ensino Medio'), ('Tecnologo ', 'Tecnólogo'), ('Ensino Superior', 'Ensino Superior'), ('POS', ' Pós / MBA / Mestrado'), ('Doutorado', 'Doutorado')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='vagas',
            name='faixa_salarial',
            field=models.CharField(choices=[('ate 1k', 'Ate 1k'), ('1k a 2k', '1k a 2k'), ('2k a 3k', '2k a 3K'), ('3k+', 'Acima de 3k')], max_length=10),
        ),
    ]