# Generated by Django 4.1.3 on 2022-11-18 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_alter_product_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='group',
            field=models.CharField(choices=[('pc', 'pc'), ('accessories', 'accessories'), ('mobile', 'mobile'), ('notebook', 'notebook')], default='mobile', max_length=20),
        ),
    ]
