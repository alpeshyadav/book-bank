from django.db import models
from postgres_copy import CopyManager

# Create your models here.
class Student(models.Model):
    student_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    address = models.TextField()
    gender = models.CharField(max_length=6)
    contact_no = models.BigIntegerField()
    parent_contact = models.BigIntegerField()
    college_name = models.TextField()
    branch_name = models.TextField()
    stream_name = models.TextField()
    current_year = models.TextField()

class CurrentYear(models.Model):
    current_year = models.CharField(max_length=50)
    objects = CopyManager()

class Stream(models.Model):
    stream_name = models.CharField(max_length=50)
    objects = CopyManager()

class Branch(models.Model):
    branch_name = models.CharField(max_length=50)
    objects = CopyManager()

class Book(models.Model):
    book_name = models.CharField(max_length=60)
    book_id = models.IntegerField(primary_key=True)
    sem = models.CharField(default=None, null=True, max_length=20)
    paper = models.CharField(default=None, null=True, max_length=20)
    author_name = models.CharField(max_length=50)
    book_edition = models.CharField(null=True, max_length=50)
    barcode = models.CharField(max_length=20)
    publisher = models.CharField(max_length=50)
    price = models.IntegerField(null=True)
    purchase_year = models.DateTimeField(null=True)
    objects = CopyManager()


class College(models.Model):
    college_name = models.CharField(max_length=40)
    objects = CopyManager()

class Author(models.Model):
    author_name = models.CharField(max_length=40)
    objects = CopyManager()

class Publisher(models.Model):
    publisher = models.CharField(max_length=40)
    objects = CopyManager()