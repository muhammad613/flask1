# Generated by Django 4.2.7 on 2023-11-30 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production_records', '0017_alter_expense_fabric'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='accessories',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='other',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='sewing',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='threads',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='productionrecord',
            name='model',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='productionrecord',
            name='name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='productionrecord',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='productionrecord',
            name='quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='productionrecord',
            name='received_by',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='windowexpense',
            name='fittings',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='windowexpense',
            name='frame',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='windowexpense',
            name='glass',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='windowexpense',
            name='installation',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='windowexpense',
            name='other',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='windowexpense',
            name='window_model_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='windowfactoryrecord',
            name='model',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='windowfactoryrecord',
            name='name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='windowfactoryrecord',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='windowfactoryrecord',
            name='quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='windowfactoryrecord',
            name='received_by',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]