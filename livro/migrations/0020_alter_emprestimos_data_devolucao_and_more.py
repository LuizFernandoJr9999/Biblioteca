# Generated by Django 5.0 on 2024-01-25 22:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0019_alter_emprestimos_data_emprestimo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimos',
            name='data_devolucao',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='emprestimos',
            name='data_emprestimo',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 25, 19, 30, 22, 283558)),
        ),
    ]
