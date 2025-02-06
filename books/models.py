from django.db import models

class Book(models.Model):
    bookID = models.AutoField(primary_key=True)  # Autoincrement primary key

    # Essential book details
    title = models.CharField(max_length=255)  # Required
    author = models.CharField(max_length=255)  # Required
    callNumber = models.CharField(max_length=100, unique=True, blank=True, null=True)  # Unique call number

    # Publication & identification details
    publisher = models.CharField(max_length=255, blank=True, null=True)
    isbn = models.CharField(max_length=50, blank=True, null=True)
    barcode = models.CharField(max_length=100, blank=True, null=True)
    year_published = models.CharField(max_length=10, blank=True, null=True)
    
    # Library location and descriptive info
    shelfNumber = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    language = models.CharField(max_length=100, blank=True, null=True)
    subject = models.CharField(max_length=255, blank=True, null=True)
    genre = models.CharField(max_length=100, blank=True, null=True)
    
    # Financial & acquisition info
    value = models.IntegerField(blank=True, null=True)
    method = models.CharField(max_length=100, blank=True, null=True)
    
    # Administrative fields
    dateAdded = models.DateTimeField(auto_now_add=True)
    availability = models.CharField(max_length=50, default='Available')
    timesBorrowed = models.IntegerField(default=0)
    condition = models.CharField(max_length=50, default='Good')

    def __str__(self):
        return f"{self.title} by {self.author}"
