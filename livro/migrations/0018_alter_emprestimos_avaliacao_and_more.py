# Generated by Django 5.0 on 2024-01-25 20:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0017_emprestimos_avaliacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimos',
            name='avaliacao',
            field=models.CharField(blank=True, choices=[('P', 'Péssimo'), ('R', 'Ruim'), ('B', 'Bom'), ('O', 'Ótimo')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='emprestimos',
            name='data_emprestimo',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 25, 17, 49, 8, 759139)),
        ),
    ]