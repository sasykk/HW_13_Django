from django.contrib import admin
from .models import Tag, Author, Quote

# Register your models here.

admin.site.register(Tag)
admin.site.register(Author)
admin.site.register(Quote)