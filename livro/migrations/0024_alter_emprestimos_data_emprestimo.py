# Generated by Django 5.0 on 2024-02-14 15:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0023_alter_emprestimos_data_emprestimo_alter_livros_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimos',
            name='data_emprestimo',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 14, 12, 28, 47, 906167)),
        ),
    ]
