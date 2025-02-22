from django.shortcuts import redirect, render, HttpResponse
from myapp.models import Quote
from django.db.models import Q

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
    quotes = Quote.objects.all()
    return render(request, 'quotes.html',{
        'quotes': quotes
    })

def create_quote2(request, content, author, origin, public):
    quote = Quote(
        content = content,    
        origin = author,
        author = origin,
        public = public
    )
    quote.save()
    return HttpResponse("Quote created")

def create_quote(request):    
    return render(request, 'createQuote.html')

def save_quote(request):
    quote_content = request.POST['quote_content']
    quote_author = request.POST['quote_author']
    quote_source = request.POST['quote_source']
    quote_public = request.POST['quote_public']

    quote = Quote(
        content = quote_content,    
        author = quote_author,
        origin = quote_source,
        public = quote_public
    )
    quote.save()
    return redirect('quotes')

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

def delete_quote(request, id):
    try:
        quote = Quote.objects.get(pk=id)
        quote.delete()        
    except:
        print("There was an error")
    return redirect('quotes')