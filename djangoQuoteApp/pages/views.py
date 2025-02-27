from django.shortcuts import redirect, render
from .models import Page

# Create your views here.
def index(request):
    page = Page.objects.get(slug='home')

    return render(request, "page.html", {
        'page': page
    })

def page(request, slug='home'):
    page = Page.objects.get(slug=slug)

    return render(request, "page.html", {
        'page': page
    })