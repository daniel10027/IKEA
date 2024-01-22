from django.db import models
from autoslug import AutoSlugField
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
from django.urls import reverse
from tinymce.models import HTMLField



class Categorie(models.Model):

    """Model definition for Categorie."""
    titre = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='titre')
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Categorie."""

        verbose_name = 'Categorie'
        verbose_name_plural = 'Categories'
        ordering = ['titre']

    def __str__(self):
        """Unicode representation of Categorie."""
        return self.titre

    @property
    def produits(self):
        return self.product_categorie.all()

    @property
    def huits(self):
        return self.product_categorie.all().order_by('-created')[:8]


    def url(self):
        """Return absolute url for Ticket."""
        return reverse("categorie-detail", 
        kwargs={"slug": self.slug, "pk": self.pk,})
        

    # TODO: Define custom methods here




class Produit(models.Model):
    """Model definition for Produit."""
    titre       = models.CharField(max_length=50)
    categorie   = models.ForeignKey(Categorie, related_name="product_categorie", on_delete=models.CASCADE)
    image       = models.ImageField(upload_to='categorie/images', max_length = 100)
    fichier_3d = models.FileField(upload_to='categorie/images', max_length=100, blank=True )
    description = HTMLField()
    prix        = models.IntegerField(default=0)
    en_promo    = models.BooleanField(default=False)
    pourcentage_promo = models.IntegerField(default=0)
    active      = models.BooleanField(default=True)
    have_3d_viewer      = models.BooleanField(default=False)
    created     = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    slug        = AutoSlugField(populate_from='titre')

    # TODO: Define fields here

    class Meta:
        """Meta definition for Produit."""

        verbose_name = 'Produit'
        verbose_name_plural = 'Produits'
        ordering = ['-created']

    def __str__(self):
        """Unicode representation of Produit."""
        return self.titre

    def save(self):
        """Save method for ImageProduit."""
        im = Image.open(self.image)
        output = BytesIO()
        im = im.resize( (275,275) )
        im.save(output, format='PNG', quality=100)
        output.seek(0)
        self.image = InMemoryUploadedFile(output,'ImageField', "%s.png" %self.image.name.split('.')[0], 'image/png', sys.getsizeof(output), None)
        super(Produit,self).save()

    def get_absolute_url(self):
        """Return absolute url for Produit."""
        return ('')

    def url(self):
        """Return absolute url for Ticket."""
        return reverse("product_details", 
        kwargs={"slug": self.slug, "pk": self.pk,})

    @property
    def price(self):
        if self.en_promo:

            a = int(self.prix -  (self.prix  * self.pourcentage_promo) / 100)
            return a
        else:
            return self.prix

    # TODO: Define custom methods here
    @property
    def images(self):
        return self.product_image.order_by('-created')
    

    @property
    def imageUrl(self):
        return self.image.url


# Create your models here.
class ImageProduit(models.Model):
    """Model definition for ImageProduit."""
    produit   = models.ForeignKey(Produit, related_name="product_image", on_delete=models.CASCADE)
    image       = models.ImageField(upload_to='products/images',default="none.jpg", max_length = 100)
    active      = models.BooleanField(default=True)
    created     = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    # TODO: Define fields here

    class Meta:
        """Meta definition for ImageProduit."""

        verbose_name = 'Image Produit'
        verbose_name_plural = 'Image Produits'

    def __str__(self):
        """Unicode representation of Image Produit."""
        return self.produit.titre

    def save(self):
        """Save method for ImageProduit."""
        im = Image.open(self.image)
        output = BytesIO()
        im = im.resize( (275,275) )
        im.save(output, format='PNG', quality=100)
        output.seek(0)
        self.image = InMemoryUploadedFile(output,'ImageField', "%s.png" %self.image.name.split('.')[0], 'image/png', sys.getsizeof(output), None)
        super(ImageProduit,self).save()

    def get_absolute_url(self):
        """Return absolute url for ImageProduit."""
        return ('')

    # TODO: Define custom methods here
