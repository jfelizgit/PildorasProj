# Generated by Django 4.1 on 2022-09-29 03:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lineapedidos',
            old_name='pedido_id',
            new_name='pedido',
        ),
        migrations.RenameField(
            model_name='lineapedidos',
            old_name='producto_id',
            new_name='producto',
        ),
    ]
