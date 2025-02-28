from django.contrib import admin
from .models import Page

# Extra configuration
class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('title', 'content', 'slug')
    list_filter = ('visible',)
    list_display = ('title', 'visible', 'created_at')

# Register your models here.
admin.site.register(Page, PageAdmin)