from django.shortcuts import render
from django.views import generic

from .models import Book, BookInstance, Author, Genre, Language


def index(request):
    """
    View function for home page of site
    :param request:
    :return:
    """
    # Generate count of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()  # all() is implied by default.

    num_books_miss = Book.objects.filter(title__contains='miss').count()
    num_genre_miss = Genre.objects.filter(name__contains='miss').count()

    # Render the HTML template index. html with the data in the context variable
    return render(
        request,
        'catalog/index.html',
        context={
            'num_books': num_books,
            'num_instances': num_instances,
            'num_instances_available': num_instances_available,
            'num_authors': num_authors,
            'num_books_miss': num_books_miss,
            'num_genre_miss': num_genre_miss,
        }
    )


class BookListView(generic.ListView):
    model = Book
    paginate_by = 2


class BookDetailView(generic.DetailView):
    model = Book


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 2


class AuthorDetailView(generic.DetailView):
    model = Author
