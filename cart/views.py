from django.shortcuts import render
from .models import *
from product.models import *
from django.http import JsonResponse
import json

from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def cart(request):
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
        'items' : items,
        'order': order,
        'cartItems' : cartItems, 
        'shipping' : True,
    }
    return render(request,'sites/cart.html', context=context)


def checkout(request):
    if request.method == 'POST':
        # Vérifier si l'ID de la commande est valide
            try:
                order = Order.objects.get(customer=request.user.customer, complete=False)
            except Order.DoesNotExist:
                messages.error(request, 'La commande spécifiée n\'existe pas ou est déjà complète.')
                return redirect('checkout')

            # Mettre à jour la commande et rediriger vers l'index avec un message de succès
            order.complete = True
            order.save()
            
            # Envoyer un e-mail avec les informations de la commande
            destinataires = ['moderneoh@gmail.com']  # Remplacez par votre adresse e-mail
            sujet = "Nouvelle commande d'Article Moderneo Home"
            contenu = f'Informations de la commande:\n\n'
            contenu += f'Client: {order.customer.user.first_name} {order.customer.user.last_name}\n'
            contenu += f'Total de la commande: {order.get_cart_total} XOF\n\n'
            contenu += 'Détails de la commande:\n'
            for item in order.order_itmes.all():
                contenu += f'Produit: {item.Produit.titre}\n'
                contenu += f'Quantité: {item.quantity}\n'
                contenu += f'Prix unitaire: {item.price} XOF\n'
                contenu += f'Sous-total: {item.get_total} XOF\n\n'
            
            # Envoyer l'e-mail
            send_mail(sujet, contenu, 'moderneoh@gmail.com', destinataires, fail_silently=False)
            
            messages.success(request, 'La commande a été soumise avec succès, vous serez contacté dans les plus brefs délais!')
            return redirect('index')
        
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
        'items' : items,
        'order': order,
        'cartItems' : cartItems, 
        'shipping' : True,
       
    }
    return render(request, 'sites/checkout.html', context=context)

def wishlist(request):
    return render(request,'sites/wishlist.html')


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    customer = request.user.customer
    product = Produit.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, Produit=product)
    
    if action == "add":
        orderItem.quantity = (orderItem.quantity + 1)
        reponse = "added"
    elif action == "remove":
        orderItem.quantity = (orderItem.quantity - 1)
        reponse = "remove"
    orderItem.save()
    
    if orderItem.quantity <= 0:
        orderItem.delete()
        reponse = "deleted"
        
    if action == "delete":
        orderItem.delete()
        reponse = "deleted"
    
    return JsonResponse(reponse, safe=False)


def orderdetails(request,pk):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.order_itmes.all()
        cartItems = order.get_cart_items
        orderDetails = Order.objects.get(pk=pk)
    else: 
        items = []
        order = {'get_cart_total': 0,'get_cart_items': 0}
        cartItems = order['get_cart_items']
    
    context = {
        'items' : items,
        'order': order,
        'cartItems' : cartItems, 
        'shipping' : True,
        'orderDetails' : orderDetails,
    }
    return render(request,'sites/order-details.html', context=context)