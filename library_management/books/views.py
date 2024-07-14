from books.models import Book
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_http_methods
import json
from django.shortcuts import get_object_or_404

@require_http_methods(["GET"])
def book_list(request):
    books = Book.objects.all()
    data = [{
        "id": book.id, 
        "title": book.title, 
        "author": book.author, 
        "published_date": book.published_date, 
        "isbn_number": book.isbn_number, 
        "price": book.price} for book in books]
    return JsonResponse(data, safe=False,status = 200)

@require_http_methods(["GET"])
def book_detail(request, pk):
    
    book = get_object_or_404(Book, pk= pk)
    
    data = {
        "id": book.id, 
        "title": book.title, 
        "author": book.author, 
        "published_date": book.published_date, 
        "isbn_number": book.isbn_number, 
        "price": book.price}

    return JsonResponse(data)

@require_http_methods(["POST"])
def book_create(request):

    data = json.loads(request.body)

    book = Book(title=data["title"], author=data["author"], published_date=data["published_date"], isbn_number=data["isbn_number"], price=data["price"])


    book.save()

    return JsonResponse({"id": book.id, "title": book.title, "author": book.author, "published_date": book.published_date, "isbn_number": book.isbn_number, "price": book.price})
