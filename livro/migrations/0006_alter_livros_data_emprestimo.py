# Generated by Django 5.0 on 2023-12-26 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0005_alter_livros_data_cadastro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livros',
            name='data_emprestimo',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
