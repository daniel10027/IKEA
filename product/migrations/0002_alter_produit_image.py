# Generated by Django 5.0.1 on 2024-01-19 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='image',
            field=models.ImageField(upload_to='categorie/images'),
        ),
    ]