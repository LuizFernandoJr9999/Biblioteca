# Generated by Django 5.0 on 2024-02-14 16:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0025_alter_emprestimos_data_emprestimo_alter_livros_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimos',
            name='data_emprestimo',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 14, 13, 35, 21, 55178)),
        ),
    ]
