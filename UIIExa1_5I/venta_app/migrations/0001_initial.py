# Generated by Django 5.1 on 2024-10-28 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id_venta', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('estado', models.PositiveSmallIntegerField()),
                ('cantidad', models.PositiveIntegerField()),
                ('precio_total', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
