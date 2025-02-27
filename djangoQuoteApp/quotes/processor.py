from .models import Category, Quote

def get_categories(request):
    ids_cat_in_use = Quote.objects.filter(public=True).values_list('categories', flat=True)
    categories = Category.objects.filter(id__in=ids_cat_in_use).values_list('id', 'name')
    return {
        'categories': categories,
        'ids': ids_cat_in_use
    }
