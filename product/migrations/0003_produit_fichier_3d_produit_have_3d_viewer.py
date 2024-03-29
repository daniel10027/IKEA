# Generated by Django 5.0.1 on 2024-01-19 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_produit_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='produit',
            name='fichier_3d',
            field=models.FileField(blank=True, upload_to='categorie/images'),
        ),
        migrations.AddField(
            model_name='produit',
            name='have_3d_viewer',
            field=models.BooleanField(default=False),
        ),
    ]
