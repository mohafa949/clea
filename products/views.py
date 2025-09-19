from django.shortcuts import render

# Create your views here.
from .models import Product, News, Partner

def home(request):
    products = Product.objects.all()
    news_items = News.objects.all()
    partners = Partner.objects.all()
    return render(request, "products/Test6.html", {
        "products": products,
        "news_items": news_items,
        "partners": partners,
    })
