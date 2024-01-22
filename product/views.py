from django.shortcuts import render
from cart.models import Order
from product.models import Produit, Categorie
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.shortcuts import get_object_or_404


# Create your views here.
def order_tracking(request):
    return render(request,'sites/order-tracking.html')

class ShopListView(ListView):
    model = Produit
    template_name = 'sites/shop.html'
    context_object_name = 'produits'
    paginate_by = 12

    def get_queryset(self):
        queryset = Produit.objects.all()

        # Filtrer par tri
        sort_by = self.request.GET.get('sort_by')
        if sort_by == 'price':
            queryset = queryset.order_by('prix')
        elif sort_by == 'promo':
            queryset = queryset.filter(en_promo=True).order_by('-created')

        # Filtrer par recherche
        search_query = self.request.GET.get('search')
        if search_query:
            queryset = queryset.filter(
                Q(titre__icontains=search_query) |
                Q(categorie__titre__icontains=search_query) |
                Q(description__icontains=search_query) |
                Q(prix__icontains=search_query)
            )

        # Filtrer par catégories
        categories_query = self.request.GET.getlist('categories')
        if categories_query:
            queryset = queryset.filter(categorie__id__in=categories_query)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = Paginator(self.get_queryset(), self.paginate_by)
        page = self.request.GET.get('page')

        try:
            produits = paginator.page(page)
        except PageNotAnInteger:
            produits = paginator.page(1)
        except EmptyPage:
            produits = paginator.page(paginator.num_pages)
            
        if self.request.user.is_authenticated:
            customer = self.request.user.customer
            order, created = Order.objects.get_or_create(customer=customer, complete=False)
            items = order.order_itmes.all()
            cartItems = order.get_cart_items
        else: 
            items = []
            order = {'get_cart_total': 0,'get_cart_items': 0}
            cartItems = order['get_cart_items']

        context['produits'] = produits
        context['categories'] = Categorie.objects.all().order_by('titre')
        context['last_product'] = Produit.objects.all().order_by('-created')[:3]
        context['details'] = True
        context['listed'] = True
        context['items'] = items
        context['order'] = order
        context['cartItems'] = cartItems
        return context

class ProductDetailView(DetailView):
    model = Produit
    template_name = 'sites/product-details.html'
    context_object_name = 'produit'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_object(self, queryset=None):
        # Vous pouvez utiliser à la fois 'pk' et 'slug' pour rechercher l'objet
        queryset = queryset or self.get_queryset()
        pk = self.kwargs.get('pk')
        slug = self.kwargs.get('slug')
        if pk:
            return get_object_or_404(queryset, pk=pk)
        elif slug:
            return get_object_or_404(queryset, slug=slug)
        raise AttributeError("La vue {} nécessite une clé primaire (pk) ou un slug (slug).".format(self.__class__.__name__))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Ajoutez les produits de la même catégorie au contexte
        if self.object:
            context['produits_same_category'] = Produit.objects.filter(categorie=self.object.categorie).exclude(pk=self.object.pk)[:3]
        context['details'] = True
        if self.request.user.is_authenticated:
            customer = self.request.user.customer
            order, created = Order.objects.get_or_create(customer=customer, complete=False)
            items = order.order_itmes.all()
            cartItems = order.get_cart_items
        else: 
            items = []
            order = {'get_cart_total': 0,'get_cart_items': 0}
            cartItems = order['get_cart_items']

       
        context['categories'] = Categorie.objects.all().order_by('titre')
        context['last_product'] = Produit.objects.all().order_by('-created')[:3]
        context['details'] = True
        context['listed'] = True
        context['items'] = items
        context['order'] = order
        context['cartItems'] = cartItems
        return context

def product_details(request):
    context = {
        'three' : True
    }
    return render(request,'sites/product-details.html', context=context)

def shoplist(request):
    return render(request,'sites/shop-list.html')

