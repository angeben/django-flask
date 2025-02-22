from django.shortcuts import redirect, render, HttpResponse
from myapp.models import Quote

# Create your views here.

# Home Page
def index(request):
    return render(request, 'index.html',{
        'tools': ['Python', 'Django', 'HTML', 'CSS']
    })

def helloWorld(request):
    return render(request, 'helloWorld.html')

def contact(request):
    return render(request, 'contact.html')

def sayHi(request, name=""):
    if name.lower() == "world":
        return redirect('helloWorld')
    else:
        return render(request, 'sayHi.html',{
            'name': name,
            'title': 'Greeting Page'
        })
    
def quotes(request):
    return render(request, 'quotes.html')

def create_quote(request, content, author, origin, public):
    quote = Quote(
        content = content,    
        origin = author,
        author = origin,
        public = public
    )
    quote.save()
    return HttpResponse("Quote created")

def get_quote(request, id):
    try:
        quote = Quote.objects.get(pk=id)
        response = HttpResponse(f"Quote: {quote.content}")
    except:
        response = HttpResponse("Quote not found")
    return response

def edit_quote(request, id):
    try:
        quote = Quote.objects.get(pk=id)
        quote.content = "New " + quote.content
        quote.save()
        response = HttpResponse(f"Quote: {quote.content}")
    except:
        response = HttpResponse("Quote not found in edit")
    return response