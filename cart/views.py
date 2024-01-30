from django.shortcuts import render
from .models import *
from product.models import *
from django.http import JsonResponse
import json

from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

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


@csrf_exempt
def checkout(request):
    if request.method == 'POST':
            order_id = request.POST.get('order_id')
            # Vérifier si l'ID de la commande est valide
            try:
                order = Order.objects.get(id=order_id, customer=request.user.customer, complete=False)
            except Order.DoesNotExist:
                messages.error(request, 'La commande spécifiée n\'existe pas ou est déjà complète.')
                return redirect('checkout')

            # Mettre à jour la commande et rediriger vers l'index avec un message de succès
            order.complete = True
            order.save()
            messages.success(request, 'La commande a été soumise avec succes avec succès, vous serez contacté dans les plus Bref delais!')
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