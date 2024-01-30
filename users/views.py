
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes,  force_str
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import login
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.utils.translation import gettext as _
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from .models import Customer
from cart.models import *
from product.models import *
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def login(request):
    return render(request,'sites/login.html')

def signup(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            first_name = request.POST.get('firstname')
            last_name = request.POST.get('lastname')
            email = request.POST.get('username')  # Utilisez 'username' car le champ dans le formulaire est 'username'
            password = request.POST.get('password')
            password2 = request.POST.get('password2')

            # Vérifier si le mot de passe et la confirmation du mot de passe sont identiques
            if password == password2:
                # Vérifier si l'email ou le nom d'utilisateur existe déjà
                if User.objects.filter(email=email).exists() or User.objects.filter(username=username).exists():
                    messages.error(request, _('Un compte avec ce email existe déjà.'))
                else:
                    # Valider le mot de passe
                        # Créer un utilisateur
                        user = User.objects.create_user(username=username, email=email, password=password)
                        user.first_name = first_name
                        user.last_name = last_name
                        user.is_active = False
                        user.save()

                        # Generate an activation token and send an activation email
                        token = default_token_generator.make_token(user)
                        uid = urlsafe_base64_encode(force_bytes(user.pk))
                        activation_link = f"{get_current_site(request)}/accounts/activate/{uid}/{token}/"

                        subject = _('Activation de Votre compte Moderneo Home Pro')
                        message = render_to_string('sites/activation_email.tpl', {
                            'user': user,
                            'activation_link': activation_link,
                        })
                        from_email = 'moderneo@gmail.com'  # Replace with your email
                        to_email = user.email
                        send_mail(subject, message, from_email, [to_email])

                        messages.success(request, _('Inscription réussie! Veuillez vérifier votre e-mail pour activer votre compte.'))
                        return redirect('index')
            else:
                messages.error(request, _('Les mots de passe ne correspondent pas.'))
        except Exception as e:
            messages.error(request, _(f'Une erreur s\'est produite lors de l\'inscription. Veuillez réessayer. {e}'))
    else:
        return render(request, 'sites/signup.html')

    return render(request, 'sites/signup.html')


#activatiion des comptes
def activate_account(request, uidb64, token):
    uid = force_str(urlsafe_base64_decode(uidb64))
    user = User.objects.get(pk=uid)
    try:
        if default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            Customer.objects.create(user=user)
            messages.success(request, f'Compte {user.first_name} activé , Bienvenue sur Modernéo Home Pro')
            return redirect('login')
    except Exception as e:
        context = {
            'e':e
        }
        return render(request, 'sites/activation_error.html', context=context)


@login_required
def profile(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.order_itmes.all()
        cartItems = order.get_cart_items
        all_order = Order.objects.filter(customer=customer).order_by('complete')
    else: 
        items = []
        order = {'get_cart_total': 0,'get_cart_items': 0}
        cartItems = order['get_cart_items']
    
    context = {
        'items' : items,
        'order': order,
        'cartItems' : cartItems, 
        'shipping' : True,
        'all_order' : all_order
    }
    return render(request,'sites/profile.html', context=context)


@login_required
def adminOrder(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.order_itmes.all()
        cartItems = order.get_cart_items
        all_order = Order.objects.filter(complete=True)
    else: 
        items = []
        order = {'get_cart_total': 0,'get_cart_items': 0}
        cartItems = order['get_cart_items']
    
    context = {
        'items' : items,
        'order': order,
        'cartItems' : cartItems, 
        'shipping' : True,
        'all_order' : all_order
    }
    return render(request,'sites/order-listes.html', context=context)

from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('index')
    # Redirect to a success page.