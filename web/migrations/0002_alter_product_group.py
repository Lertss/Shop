# Generated by Django 4.1.3 on 2022-11-18 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='group',
            field=models.CharField(choices=[('mobile', 'mobile'), ('accessories', 'accessories'), ('notebook', 'notebook'), ('pc', 'pc')], default='mobile', max_length=20),
        ),
    ]