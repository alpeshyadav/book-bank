from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.urls import reverse
from datetime import timedelta
from django.contrib import messages
from django.core.serializers.json import DjangoJSONEncoder
from django.utils import timezone
from .models import Student, CurrentYear, Stream, Book, College, Branch, Author, Publisher






# Create your views here.


def index(request):
    if request.user.is_authenticated:
        return render(request, 'students/basic.html')
    else:
        return render(request, 'students/login.html')

def login_user(request):
    
    if request.method == 'GET':
        return render(request, 'students/login.html')
    username = request.POST.get('user_name')
    password = request.POST.get('password')
    print(username, password)

    user = authenticate(username=username, password=password)

    print(user)
    if user is not None:
        login(request, user)
        print(request.session.set_expiry(timezone.now() + timedelta(days=1)))
        return render(request, 'students/basic.html')
    else:
        return HttpResponse('Invalid Login Details')

# @login_required()
def student(request):
    return render(request, 'students/student_basic.html')

def add_student(request):
    print(request.method)
    if request.method == 'GET':
        current = CurrentYear.objects.all().order_by('current_year')
        stream = Stream.objects.all().order_by('stream_name')
        college = College.objects.all().order_by('college_name')
        branch = Branch.objects.all().order_by('branch_name')
        return render(request, 'students/add_student.html', {'branch':branch, 'current':current, 'college':college, 'stream':stream})
    else:
        print(request.body)
        first_name = request.POST.get('first_name').capitalize()
        last_name = request.POST.get('last_name').capitalize()
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        contact_no = request.POST.get('contact_no')
        parent_contact = request.POST.get('parent_contact')
        college_name = request.POST.get('college_name')
        branch_name = request.POST.get('branch_name')
        stream_name = request.POST.get('stream_name')
        current_year = request.POST.get('current_year')

        student_id = int(Student.objects.last().student_id)
        student_id += 1

        s = Student(student_id=student_id, first_name=first_name, last_name=last_name, gender=gender, address=address, contact_no=contact_no, parent_contact=parent_contact, college_name=college_name, branch_name=branch_name, stream_name=stream_name, current_year=current_year)
        s.save()
        current = CurrentYear.objects.all().order_by('current_year')
        stream = Stream.objects.all().order_by('stream_name')
        college = College.objects.all().order_by('college_name')
        branch = Branch.objects.all().order_by('branch_name')
        messages.success(request, f'Student Id: {student_id}')
        return HttpResponseRedirect('/student/add-student')

def search_student(request):
    if request.method == "POST":
        student_id = request.POST.get('student_id')
        first_name = request.POST.get('student_name').capitalize()
        print((student_id, first_name))
        if student_id != '':
            students = Student.objects.get(student_id=student_id)
            print(students.first_name)
            return render(request, 'students/search_student_by_id.html', {'s':students})
        
        students = Student.objects.filter(first_name=first_name)
       
        return render(request, 'students/search_student.html', {'students':students})

    else:    
        students = Student.objects.all().order_by("-student_id")
        students = Paginator(students, 50).page(1)
        return render(request, 'students/search_student.html', {'students':students,})

def book_master(request):
    return render(request, 'students/book_master.html')

def add_book(request):
    if request.method == 'GET':
        author = Author.objects.all().order_by('author_name')
        publisher = Publisher.objects.all().order_by('publisher')
        return render(request, 'students/add_book.html', {'author':author, 'publisher':publisher})
    book_name = request.POST.get('book_name')
    sem = request.POST.get('sem')
    paper = request.POST.get('paper')
    author_name = request.POST.get('author_name')
    book_edition = request.POST.get('book_edition')
    publisher = request.POST.get('publisher')
    price = request.POST.get('price')
    purchase_year = request.POST.get('purchase_year')
    print(purchase_year)
    last_book_barcode = Book.objects.last().barcode
    last_book_id = int(last_book_barcode[1:])
    last_book_id += 1
    last_book_id = str(last_book_id).zfill(8)
    barcode = 'B'+last_book_id
    book_id = int(barcode[1:])
    
    book = Book(book_id=book_id, book_name=book_name, sem=sem, paper=paper, author_name=author_name, book_edition=book_edition, barcode=barcode, publisher=publisher, price=price, purchase_year=purchase_year)
    book.save()
    messages.success(request, f'Barcode: {barcode}')

    return HttpResponseRedirect('/bookmaster/add-book')

def search_book(request): 
    if request.method == "POST":
        book_id = request.POST.get('book_id')
        barcode = request.POST.get('barcode')
        
        if book_id != '':
            books = Book.objects.get(book_id=book_id)
            print(books.book_name)
            return render(request, 'students/search_book_by_id.html', {'books':books})
        
        books = Book.objects.get(barcode=barcode)
        print(books.barcode)
        return render(request, 'students/search_book_by_id.html', {'books':books})

    else:        
        books = Book.objects.order_by('-book_id')[:50]
        return render(request, 'students/search_book.html', {'books':books})

def author_master(request):
    return render(request, 'students/author_master.html')

def add_author(request):
    if request.method == "GET":
        return render(request, 'students/add_author.html')
    author_name = request.POST.get('author_name').title()
    author = Author(author_name=author_name)
    author.save()
    return HttpResponseRedirect('/authormaster/add-author')

def search_author(request):
    if request.method == 'POST':
        author_name = request.POST.get('author_name').title()
        author = Author.objects.filter(author_name=author_name)
        return render(request, 'students/search_author.html', {'author':author})

    author = Author.objects.all().order_by('author_name')
    author = Paginator(author, 50).page(1)
    return render(request, 'students/search_author.html', {'author':author})

def college_master(request):
    return render(request, 'students/college_master.html')

def add_college(request):
    if request.method == "GET":
        return render(request, 'students/add_college.html')
    college_name = request.POST.get('college_name').title()
    college = College(college_name=college_name)
    college.save()
    return HttpResponseRedirect('/collegemaster/add-college')

def search_college(request):
    if request.method == 'POST':
        college_name = request.POST.get('college_name').title()
        college = College.objects.filter(college_name=college_name)
        return render(request, 'students/search_college.html', {'college':college})

    college = College.objects.all().order_by('college_name')
    college = Paginator(college, 50).page(1)
    return render(request, 'students/search_college.html', {'college':college})

def branch_master(request):
    return render(request, 'students/branch_master.html')

def add_branch(request):
    if request.method == "GET":
        return render(request, 'students/add_branch.html')
    branch_name = request.POST.get('branch_name').title()
    branch = Branch(branch_name=branch_name)
    branch.save()
    return HttpResponseRedirect('/branchmaster/add-branch')

def search_branch(request):
    if request.method == 'POST':
        branch_name = request.POST.get('branch_name').title()
        branch = Branch.objects.filter(branch_name=branch_name)
        return render(request, 'students/search_branch.html', {'branch':branch})

    branch = Branch.objects.all().order_by('branch_name')
    branch = Paginator(branch, 50).page(1)
    return render(request, 'students/search_branch.html', {'branch':branch})

def year_master(request):
    return render(request, 'students/year_master.html')

def add_year(request):
    if request.method == "GET":
        return render(request, 'students/add_year.html')
    current_year = request.POST.get('current_year').title()
    branch = Branch(current_year=current_year)
    branch.save()
    return HttpResponseRedirect('/yearmaster/add-year')

def search_year(request):
    if request.method == 'POST':
        branch_name = request.POST.get('branch_name').title()
        current = CurrentYear.objects.filter(current_year=current_year)
        return render(request, 'students/search_year.html', {'current':current})

    current = CurrentYear.objects.all().order_by('current_year')
    current = Paginator(current, 50).page(1)
    return render(request, 'students/search_year.html', {'current':current})

def publisher_master(request):
    return render(request, 'students/publisher_master.html')

def add_publisher(request):
    if request.method == "GET":
        return render(request, 'students/add_publisher.html')
    publisher = request.POST.get('publisher').title()
    publisher = Publisher(publisher=publisher)
    publisher.save()
    return HttpResponseRedirect('/publishermaster/add-publisher')

def search_publisher(request):
    if request.method == 'POST':
        publisher = request.POST.get('publisher').title()
        publisher = Publisher.objects.filter(publisher=publisher)
        return render(request, 'students/search_publisher.html', {'publisher':publisher})

    publisher = Publisher.objects.all().order_by('publisher')
    publisher = Paginator(publisher, 50).page(1)
    return render(request, 'students/search_publisher.html', {'publisher':publisher})

def stream_master(request):
    return render(request, 'students/stream_master.html')

def add_stream(request):
    if request.method == "GET":
        return render(request, 'students/add_stream.html')
    stream_name = request.POST.get('stream_name').title()
    stream_name = Stream(stream_name=stream_name)
    stream_name.save()
    return HttpResponseRedirect('/streammaster/add-stream')

def search_stream(request):
    if request.method == 'POST':
        stream_name = request.POST.get('stream_name').title()
        stream = Stream.objects.filter(stream_name=stream_name)
        return render(request, 'students/search_stream.html', {'stream':stream})

    stream_name = Stream.objects.all().order_by('stream_name')
    stream = Paginator(stream_name, 50).page(1)
    return render(request, 'students/search_stream.html', {'stream':stream})


def issue_book(request):
    if request.method == "GET":
        return render(request, 'students/issue_book.html')
    else:
        student_id = request.POST.get('student_id')
        if student_id != '':
            students = Student.objects.get(student_id=student_id)
            print(students.first_name)
            return render(request, 'students/issue_book.html', {'s':students})
       

def logout_user(request):
    logout(request)
    return render(request, 'students/login.html')


