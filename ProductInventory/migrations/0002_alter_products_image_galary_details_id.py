# Generated by Django 4.0.4 on 2022-05-15 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ProductInventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image_galary_details_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ProductInventory.imagegalarydetails'),
        ),
    ]
