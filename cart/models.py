from django.db import models
from autoslug import AutoSlugField
from django.urls import reverse
from django.db import models
from product.models import Produit
from autoslug import AutoSlugField
import secrets
import sys
import string
# Create your models here.

class Order(models.Model):

    """Model definition for Order."""
    customer = models.ForeignKey('users.Customer', on_delete=models.SET_NULL, related_name="user_order", blank=True, null=True)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    date_orderd = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    livre = models.BooleanField(default=False)
    transaction_id  = models.CharField(max_length=200, null=True)
    slug        = AutoSlugField(populate_from='created')
    code = models.CharField(max_length=12, editable=False)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Order."""

        verbose_name = 'Commande'
        verbose_name_plural = 'Commandes'

    def __str__(self):
        """Unicode representation of Order."""
        return str(self.id)
    @property
    def get_cart_total(self):

        orderitems = self.order_itmes.all()
        total = sum([item.get_total for item in orderitems])
        return total

    def get_cart_items(self):

        orderitems = self.order_itmes.all()
        total = sum([item.quantity for item in orderitems])
        return total
    
    @property
    def shipping(self):
        return True

    @property
    def shipping(self):
        return True


    def get_absolute_url(self):
        """Return absolute url for Order."""
        return ('')

    @property
    def status(self):
        if self.livre :
            return "Traitée"
        return " En cours de traitement"
        
    @property
    def url(self):
        """Return absolute url for Ticket."""
        return reverse("order-detail", 
        kwargs={"slug": self.slug, "pk": self.pk,})

    @property
    def items_set(self):
        return self.order_itmes.all().order_by('-created')

    @property
    def adresse(self):
        return self.order_billing.last().localite

    # TODO: Define custom methods here
    
    def save(self, *args, **kwargs):
            if not self.code:
                # Generate a random 10-character alphanumeric code
                chars = (string.ascii_uppercase + string.digits).upper()
                self.code = ''.join(secrets.choice(chars) for _ in range(12))

                # Ensure the code is unique in the database
                while Order.objects.filter(code=self.code).exists():
                    self.code = ''.join(secrets.choice(chars) for _ in range(12))

            super(Order, self).save(*args, **kwargs)


class OrderItem(models.Model):
    """Model definition for OrderItem."""
    Produit = models.ForeignKey(Produit, related_name="order_Produit", on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, related_name="order_itmes", on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0,  blank=True, null=True)
    date_added = models.DateTimeField(auto_now=True) 
    price = models.IntegerField(default=0, editable=False)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    slug        = AutoSlugField(populate_from='created')

    # TODO: Define fields here

    class Meta:
        """Meta definition for OrderItem."""

        verbose_name = 'OrderItem'
        verbose_name_plural = 'OrderItems'

    def __str__(self):
        """Unicode representation of OrderItem."""
        return "{} ({})".format(self.Produit.titre, self.id)

    def get_absolute_url(self):
        """Return absolute url for OrderItem."""
        return ('')
    
    @property
    def get_total(self):
        return self.price * self.quantity

    def save(self, *args, **kwargs):
        self.price = self.Produit.price 
        super(OrderItem, self).save(*args, **kwargs)

    # TODO: Define custom methods here


class WishList(models.Model):

    customer = models.ForeignKey('users.Customer', on_delete=models.SET_NULL, related_name="user_wish", blank=True, null=True)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    slug        = AutoSlugField(populate_from='created')
    """Model definition for WishList."""

    # TODO: Define fields here

    class Meta:
        """Meta definition for WishList."""

        verbose_name = 'Liste de souhaits'
        verbose_name_plural = 'Liste de souhaits'

    def __str__(self):
        """Unicode representation of WishList."""
        return str(self.id)

    def get_absolute_url(self):
        """Return absolute url for WishList."""
        return ('')

    @property
    def get_wish_total(self):

        wishitems = self.wishlist_itmes.all()
        total = sum([item.get_total for item in wishitems])
        return total

    def get_wish_items(self):

        wishitems = self.wishlist_itmes.all()
        total = sum([item.quantity for item in wishitems])
        return total

    @property
    def shipping(self):
        return True

    # TODO: Define custom methods here


class WishListItem(models.Model):
    """Model definition for WishListItem."""

    Produit = models.ForeignKey(Produit  ,  related_name="wishlist_Produit", on_delete=models.SET_NULL, blank=True, null=True)
    wish = models.ForeignKey(WishList    ,  related_name="wishlist_itmes"  , on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0,  blank=True, null=True)
    date_added = models.DateTimeField(auto_now=True) 
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    slug        = AutoSlugField(populate_from='created')

    # TODO: Define fields here

    class Meta:
        """Meta definition for WishListItem."""

        verbose_name = 'WishListItem'
        verbose_name_plural = 'WishListItems'

    def __str__(self):
        """Unicode representation of WishListItem."""
        return str(self.Produit)


    def get_absolute_url(self):
        """Return absolute url for WishListItem."""
        return ('')

    # TODO: Define custom methods here



class AdressseLivraison(models.Model):

    """Model definition for AdressseLivraison."""
    customer = models.ForeignKey('users.Customer', on_delete=models.SET_NULL, related_name="user_billing", blank=True, null=True)
    localite = models.CharField(max_length=50)
    nom = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    telephone = models.CharField(max_length=50)
    order    = models.ForeignKey(Order, on_delete=models.SET_NULL, related_name="order_billing", blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    slug        = AutoSlugField(populate_from='created')

    # TODO: Define fields here

    class Meta:
        """Meta definition for AdressseLivraison."""

        verbose_name = 'Adressse Livraison'
        verbose_name_plural = 'Adressse  Livraisons'

    def __str__(self):
        """Unicode representation of AdressseLivraison."""
        return str(self.id)


    def get_absolute_url(self):
        """Return absolute url for AdressseLivraison."""
        return ('')

    # TODO: Define custom methods here