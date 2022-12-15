# Generated by Django 4.1.3 on 2022-12-08 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_user', '0011_alter_transfer_status'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ReturnedProducts',
            new_name='Purchases',
        ),
        migrations.AlterModelOptions(
            name='purchases',
            options={'ordering': ('product_name', 'brand', 'price', 'unit', 'qty', 'supplier')},
        ),
        migrations.RenameField(
            model_name='purchases',
            old_name='user',
            new_name='supplier',
        ),
    ]