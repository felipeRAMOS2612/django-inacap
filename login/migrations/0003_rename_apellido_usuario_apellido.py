# Generated by Django 4.2.2 on 2023-07-09 23:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_cargo_alter_usuario_options_alter_usuario_managers_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='Apellido',
            new_name='apellido',
        ),
    ]