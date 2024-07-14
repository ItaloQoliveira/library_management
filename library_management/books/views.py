from books.models import Book
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET"])
def book_list(request):
    books = Book.objects.all()
    data = [{"id": book.id, "title": book.title, "author": book.author, "published_date": book.published_date, "isbn_number": book.isbn_number, "price": book.price} for book in books]
    return JsonResponse(data, safe=False)
    