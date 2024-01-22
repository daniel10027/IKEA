from django.shortcuts import render
from cart.models import Order
from product.models import Categorie, Produit, ImageProduit
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.order_itmes.all()
        cartItems = order.get_cart_items
    else: 
        items = []
        order = {'get_cart_total': 0,'get_cart_items': 0}
        cartItems = order['get_cart_items']
    
    context = {
        'categories' : Categorie.objects.all(),
        'produits' : Produit.objects.all(),
        'new_produits' : Produit.objects.filter(active=True).order_by('-created')[:3],
        'items' : items,
        'order': order,
        'cartItems' : cartItems, 
        'shipping' : True,
        
    }
    
    return render(request,'sites/index.html', context=context)


# Create your views here.
def about(request):
    return render(request,'sites/about.html')


def contact(request):
    
    if request.method == 'POST':
        nom = request.POST.get('nom', '')
        email = request.POST.get('email', '')
        telephone = request.POST.get('telephone', '')
        message = request.POST.get('message', '')

        destinataires = ['danielguedegbe10027@gmail.com', ]#'moderneoh@gmail.com'
        sujet = 'Nouvelle demande de rendez*Vous Moderneo Home'
        contenu = f'Nom: {nom}\n\nEmail: {email}\n\nTéléphone: {telephone}\n\nMessage: {message}'
        send_mail(sujet, contenu, 'moderneoh@gmail.com', destinataires, fail_silently=False)

        # Redirection avec un paramètre de requête pour indiquer le succès
        return HttpResponseRedirect(reverse('contact') + '?success=true')
    
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.order_itmes.all()
        cartItems = order.get_cart_items
    else: 
        items = []
        order = {'get_cart_total': 0,'get_cart_items': 0}
        cartItems = order['get_cart_items']
    
    context = {
        'categories' : Categorie.objects.all(),
        'produits' : Produit.objects.all(),
        'new_produits' : Produit.objects.filter(active=True).order_by('-created')[:3],
        'items' : items,
        'order': order,
        'cartItems' : cartItems, 
        'shipping' : True,
        
    }
    return render(request,'sites/contact.html', context=context)

def faq(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.order_itmes.all()
        cartItems = order.get_cart_items
    else: 
        items = []
        order = {'get_cart_total': 0,'get_cart_items': 0}
        cartItems = order['get_cart_items']
    
    context = {
        'categories' : Categorie.objects.all(),
        'produits' : Produit.objects.all(),
        'new_produits' : Produit.objects.filter(active=True).order_by('-created')[:3],
        'items' : items,
        'order': order,
        'cartItems' : cartItems, 
        'shipping' : True,
        
    }
    return render(request,'sites/faq.html', context=context)

def tracking(request):
    
    if request.method == 'POST':
        nom = request.POST.get('nom', '')
        telephone = request.POST.get('telephone', '')
        message = request.POST.get('message', '')

        destinataires = ['danielguedegbe10027@gmail.com', ]#'moderneoh@gmail.com'
        sujet = 'Nouvelle demande de Meuble sur Mesure Moderneo Home'
        contenu = f'Nom: {nom}\n\n Téléphone: {telephone}\n\nMessage: {message}'
        send_mail(sujet, contenu, 'moderneoh@gmail.com', destinataires, fail_silently=False)

        # Redirection avec un paramètre de requête pour indiquer le succès
        return HttpResponseRedirect(reverse('tracking') + '?success=true')
    
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.order_itmes.all()
        cartItems = order.get_cart_items
    else: 
        items = []
        order = {'get_cart_total': 0,'get_cart_items': 0}
        cartItems = order['get_cart_items']
    
    context = {
        'categories' : Categorie.objects.all(),
        'produits' : Produit.objects.all(),
        'new_produits' : Produit.objects.filter(active=True).order_by('-created')[:3],
        'items' : items,
        'order': order,
        'cartItems' : cartItems, 
        'shipping' : True,
        
    }
    return render(request,'sites/order-tracking.html', context=context)
