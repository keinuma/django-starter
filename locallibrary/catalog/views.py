from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import (
    LoginRequiredMixin, PermissionRequiredMixin
)
import datetime

from .models import (
    Book, BookInstance, Author, Genre
)
from .forms import RenewBookForm, RenewBookModelForm


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

    # Number of visits to this view, as counted in the session variable
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    # Render the HTML template index.
    # html with the data in the context variable
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
            'num_visits': num_visits,
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


class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    """
    Generic class based view listing books on loan to current user.
    """
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(
            borrower=self.request.user
        ).filter(status__exact='o').order_by('due_back')


class LoanedAllBooksListView(PermissionRequiredMixin,
                             generic.ListView):
    """
    Generic class based view listing books on loan to all user.
    """
    permission_required = 'catalog.can_mark_returned'
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_all_user.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(
            status__exact='o'
        ).order_by('due_back')


@permission_required('catalog.can_mark_returned')
def renew_book_librarian(request, pk):
    """
    View function for renewing a specific BookInstance by librarian
    """
    book_inst = get_object_or_404(BookInstance, pk=pk)

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding)
        form = RenewBookModelForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            book_inst.due_back = form.cleaned_data['due_back']
            book_inst.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('all-borrowed'))

    # If this is a FET create the default form.
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = RenewBookModelForm(initial={'due_back': proposed_renewal_date})
    return render(request,
                  'catalog/book_renew_librarians.html',
                  {'form': form, 'bookinst': book_inst})


class AuthorCreate(generic.edit.CreateView):
    model = Author
    fields = '__all__'
    initial = {'date_of_death': '05/01/2018', }


class AuthorUpdate(generic.edit.UpdateView):
    model = Author
    fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']


class AuthorDelete(generic.edit.DeleteView):
    model = Author
    success_url = reverse_lazy('author')


class BookCreate(generic.edit.CreateView):
    model = Book
    fields = '__all__'
    initial = {'title': 'テスト'}


class BookUpdate(generic.edit.UpdateView):
    model = Book
    fields = '__all__'


class BookDelete(generic.edit.DeleteView):
    model = Book
    success_url = reverse_lazy('books')
