import uuid
from django.db import models
from django.urls import reverse


class Genre(models.Model):
    """
    Model representing a book genre
    """
    name = models.CharField(
        max_length=200,
        help_text='Enter a book genre (e.g. Science Fiction, French Poetry etc.)'
    )

    def __str__(self):
        """
        Setting for representing the Model object.
        :return str self.name: genre name
        """
        return self.name


class Language(models.Model):
    """
    Model representing a book language
    """
    name = models.CharField(
        max_length=200,
        help_text='Enter a book language (e.g. English, Spanish, Japanese etc.)'
    )

    def __str__(self):
        """
        Setting for representing the Model object
        :return:
        """
        return self.name


class Book(models.Model):
    """
    Model representing a book (but not specific copy of book)
    """
    title = models.CharField(max_length=200)

    # Foreign key used because book can have only author but authors can have multiple books
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
    isbn = models.CharField('ISBN', max_length=13, help_text='13 Character for ISBN number')

    # ManyToManyField used because genre can contain many books. Books can cover many genre.
    genre = models.ManyToManyField(Genre, help_text='Select for a genre for this book')
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """
        String for representing the Model objects
        :return:
        """
        return self.title

    def get_absolute_url(self):
        """
        Returns the url access to a detail record for this book
        :return:
        """
        return reverse('book-detail', args=[str(self.id)])

    def display_genre(self):
        """
        Creates a string for the Genre. This is required to display genre in Admin.
        :return:
        """
        return ', '.join([genre.name for genre in self.genre.all()[:3]])
        display_genre.short_description = 'Genre'


class BookInstance(models.Model):
    """
    Model representing a specific copy of a book (i.e. that can be borrowed from the library)
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text='Unique ID for this particular book across whole library')
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True,
                              default='m', help_text='Book availability')

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        """
        String for representing the Model object
        :return:
        """
        return '{0} ({1})'.format(self.id, self.book.title)


class Author(models.Model):
    """
    Model representing an author.
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """
        Return the url to access a particular author instance
        :return:
        """
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the Model object
        :return:
        """
        return '{0}, {1}'.format(self.last_name, self.first_name)
