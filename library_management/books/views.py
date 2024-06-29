from typing import Any
from django.shortcuts import render
from books.models import Book
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

class BookCreateView(CreateView):
    model = Book 
    fields = ["author", "title", "published_date", "isbn_number", "price"]
    template_name_suffix = "_create_form"

class BookUpdateView(UpdateView):
    model = Book
    fields = ["author", "title", "published_date", "isbn_number", "price"]
    template_name_suffix = "_update_form"

"""class BookDetailView(DetailView):
    model = Book
"""
class BookListView(ListView):
    model = Book
    
