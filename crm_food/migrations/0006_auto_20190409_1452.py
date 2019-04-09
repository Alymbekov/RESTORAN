# Generated by Django 2.2 on 2019-04-09 08:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm_food', '0005_auto_20190409_0042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='check',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='crm_food.Order'),
        ),
        migrations.AlterField(
            model_name='order',
            name='table',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='crm_food.Table'),
        ),
    ]
