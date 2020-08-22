from django.contrib import admin
from .models import Student, CurrentYear, Stream, Book, College, Branch, Author, Publisher
# Register your models here.
admin.site.register(Student)
admin.site.register(CurrentYear)
admin.site.register(Stream)
admin.site.register(Book)
admin.site.register(College)
admin.site.register(Branch)
admin.site.register(Author)
admin.site.register(Publisher)
