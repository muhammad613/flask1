# Generated by Django 4.2.7 on 2023-11-21 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production_records', '0006_delete_expenserecord_alter_productionrecord_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('fabric', models.CharField(max_length=100)),
                ('sewing', models.CharField(max_length=100)),
                ('threads', models.CharField(max_length=100)),
                ('accessories', models.CharField(max_length=100)),
                ('other', models.CharField(max_length=100)),
                ('total', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
        ),
    ]
