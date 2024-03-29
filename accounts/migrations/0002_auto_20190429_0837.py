# Generated by Django 2.0 on 2019-04-29 08:37

import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'usuario', 'verbose_name_plural': 'usuarios'},
        ),
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='fecha de alta'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=70, unique=True, verbose_name='Correo electrónico'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='nombre'),
        ),
        migrations.AlterField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='Los grupos a los que pertenece este usuario. Un usuario tendrá todos los permisos asignados a cada uno de sus grupos.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='grupos'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Indica si el usuario debe ser tratado como activo. Desmarque esta opción en lugar de borrar la cuenta.', verbose_name='activo'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False, help_text='Indica si el usuario puede entrar en este sitio de administración.', verbose_name='es staff'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Indica que este usuario tiene todos los permisos sin asignárselos explícitamente.', verbose_name='es superusuario'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='último inicio de sesión'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='apellidos'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=128, verbose_name='contraseña'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Permisos específicos para este usuario.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='permisos de usuario'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(error_messages={'unique': 'Ya existe un usuario con este nombre.'}, help_text='Requerido. 150 carácteres como máximo. Únicamente letras, dígitos y @/./+/-/_ ', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='nombre de usuario'),
        ),
    ]
