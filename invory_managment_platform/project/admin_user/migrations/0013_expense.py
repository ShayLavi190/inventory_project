# Generated by Django 4.1.3 on 2022-12-09 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_user', '0012_rename_returnedproducts_purchases_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=30)),
                ('reference', models.CharField(max_length=30)),
                ('date', models.DateField()),
                ('price', models.CharField(max_length=40)),
            ],
            options={
                'ordering': ('description', 'reference', 'date', 'price'),
            },
        ),
    ]
