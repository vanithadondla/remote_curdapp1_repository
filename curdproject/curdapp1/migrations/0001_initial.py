# Generated by Django 2.0.5 on 2019-05-29 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField()),
                ('product_name', models.CharField(max_length=50)),
                ('product_cost', models.IntegerField()),
                ('product_color', models.CharField(max_length=100)),
                ('product_class', models.CharField(max_length=100)),
                ('customer_name', models.CharField(max_length=100)),
                ('customer_mobile', models.BigIntegerField()),
                ('customer_email', models.EmailField(max_length=100)),
            ],
        ),
    ]
