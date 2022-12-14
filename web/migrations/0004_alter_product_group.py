# Generated by Django 4.1.3 on 2022-11-19 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_alter_product_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='group',
            field=models.CharField(choices=[('notebook', 'notebook'), ('mobile', 'mobile'), ('pc', 'pc'), ('accessories', 'accessories')], default='mobile', max_length=20),
        ),
    ]