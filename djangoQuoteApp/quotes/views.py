from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from quotes.forms import QuoteForm
from quotes.models import Quote
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def quotes(request, category_id=0):
    ids_cat_in_use = Quote.objects.filter(public=True).values_list('categories', flat=True)
    if category_id in ids_cat_in_use:
        quotes = Quote.objects.filter(public=True, categories=category_id).order_by('-updated_at')
    else:
        quotes = Quote.objects.filter(public=True).order_by('-updated_at')

    paginator = Paginator(quotes, 2)
    page = request.GET.get('page')
    page_quotes = paginator.get_page(page)

    return render(request, 'quotes.html',{
        'quotes': page_quotes
    })

@login_required(login_url='login')
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
                public = quote_public,
                user = request.user
            )
            quote.save()
            return redirect('quotes')
    else:
        form = QuoteForm() 
    return render(request, 'createQuote.html', {
        'form': form,
        'quoteAction': 'Create Quote'
    })

@login_required(login_url='login')
def get_quote(request, id):
    try:
        quote = Quote.objects.get(pk=id)
        response = HttpResponse(f"Quote: {quote.content}")
    except:
        response = HttpResponse("Quote not found")
    return response

@login_required(login_url='login')
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

@login_required(login_url='login')
def delete_quote(request, id):
    try:
        quote = Quote.objects.get(pk=id)
        quote.delete()        
    except:
        print("There was an error")
    return redirect('quotes')