# Generated by Django 4.0.4 on 2022-05-28 02:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': '댓글', 'verbose_name_plural': '댓글'},
        ),
        migrations.AlterModelTable(
            name='comment',
            table='Comment',
        ),
    ]
