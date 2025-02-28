from django.contrib import admin
from .models import Category, Quote

class QuoteAdmin(admin.ModelAdmin):
    readonly_fields = ('user', 'created_at', 'updated_at')
    search_fields = ('content', 'origin', 'author', 'user__username','categories__name')
    list_filter = ('public',)
    list_display = ('content', 'user__username', 'public', 'created_at')
    ordering = ('-created_at',)
    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user_id = request.user.id
        obj.save()

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)
    search_fields = ('name',)

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Quote, QuoteAdmin)