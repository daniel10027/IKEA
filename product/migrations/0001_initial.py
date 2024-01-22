# Generated by Django 5.0.1 on 2024-01-19 12:45

import autoslug.fields
import django.db.models.deletion
import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=50)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='titre')),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Categorie',
                'verbose_name_plural': 'Categories',
                'ordering': ['titre'],
            },
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=50)),
                ('image', models.ImageField(default='none.jpg', upload_to='categorie/images')),
                ('description', tinymce.models.HTMLField()),
                ('prix', models.IntegerField(default=0)),
                ('en_promo', models.BooleanField(default=False)),
                ('pourcentage_promo', models.IntegerField(default=0)),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='titre')),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_categorie', to='product.categorie')),
            ],
            options={
                'verbose_name': 'Produit',
                'verbose_name_plural': 'Produits',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='ImageProduit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='none.jpg', upload_to='products/images')),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_image', to='product.produit')),
            ],
            options={
                'verbose_name': 'Image Produit',
                'verbose_name_plural': 'Image Produits',
            },
        ),
    ]
