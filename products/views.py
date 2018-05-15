from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, TemplateView, CreateView, DetailView, UpdateView
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Product
# Create your views here.
#def home(request):
#    products = Product.objects
#    return render(request, 'products/home.html',{'products':products})

class ProductListView(ListView):
    context_object_name = 'products'
    model = Product

class ProductDetailView(DetailView):
    model = Product

@login_required(login_url="/accounts/signup")
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body'] and request.FILES['image'] and request.FILES['icon']:
            product = Product()
            product.title = request.POST['title']
            product.body = request.POST['body']
            product.icon = request.FILES['icon']
            product.image = request.FILES['image']
            product.pub_date = timezone.datetime.now()
            product.hunter = request.user
            product.save()
            return redirect('/products/' + str(product.id))
        else:
            return render(request, 'products/product_form.html', {'error': 'All fields are required'})
    else:
        return render(request, 'products/product_form.html')



@login_required(login_url="/accounts/signup")
def upvote(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=product_id)
        product.votes_total += 1
        product.save()
        return redirect('/products/' + str(product.id))
