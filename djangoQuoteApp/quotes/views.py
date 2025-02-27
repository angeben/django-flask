from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from quotes.forms import QuoteForm
from quotes.models import Quote, Category

# Create your views here.
def quotes(request, category_id=0):
    if category_id in range(1,5):
        quotes = Quote.objects.filter(public=True, categories=category_id)
    else:
        quotes = Quote.objects.filter(public=True)
    return render(request, 'quotes.html',{
        'quotes': quotes
    })

def create_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        # Validation and data management
        if form.is_valid():
            form_data = form.cleaned_data
            quote_content = form_data.get('content')
            quote_author = request.POST['author']
            quote_source = form_data['origin']
            quote_public = form_data['public']
            quote = Quote(
                content = quote_content,    
                author = quote_author,
                origin = quote_source,
                public = quote_public
            )
            quote.save()
            return redirect('quotes')
    else:
        form = QuoteForm() 
    return render(request, 'createQuote.html', {
        'form': form,
        'quoteAction': 'Create Quote'
    })

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
        if request.method == 'POST':
            form = QuoteForm(request.POST)
            # Validation and data management
            if form.is_valid():
                form_data = form.cleaned_data
                quote.content = form_data.get('content')
                quote.author = request.POST['author']
                quote.origin = form_data['origin']
                quote.public = form_data['public']
                quote.save()
                return redirect('quotes')
        else:
            form = QuoteForm()
        return render(request, 'createQuote.html', {
            'form': form,
            'quoteAction': 'Update Quote'
        })
    except:
        return redirect('quotes')

def delete_quote(request, id):
    try:
        quote = Quote.objects.get(pk=id)
        quote.delete()        
    except:
        print("There was an error")
    return redirect('quotes')