from django.contrib import admin

# Register your models here
from .models import BooksModel
# Register your models here.

admin.site.register(BooksModel)