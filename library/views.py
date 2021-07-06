from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect

from .forms import *


# Create your views here.

def index(request):
    return render(request, 'index.html')


@login_required(login_url='/admin/login/')
def books(request):
    all_books = Books.objects.all()
    if request.method == "POST":
        form = BookForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'New Book Added')
        else:
            print(form.errors)
            messages.error(request, form.errors)
        return redirect('books')

    elif request.method == "GET":
        query = request.GET.get("q", None)
        objects = Books.objects.all()
        if query is not None:
            all_books = objects.filter(Q(isbn__icontains=query) | Q(author__icontains=query) | Q(name__icontains=query))

    paginator = Paginator(all_books, 7)
    page = request.GET.get('pg')
    all_books = paginator.get_page(page)

    return render(request, 'books.html', {'all_books': all_books})


@login_required(login_url='/admin/login/')
def persons(request):
    all_persons = Person.objects.all()

    if request.method == "POST":
        form = PersonForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, 'New Person Added')
        else:
            print(form.errors)
            messages.error(request, form.errors)
        return redirect('persons')

    elif request.method == "GET":
        query = request.GET.get("q", None)
        objects = Person.objects.all()
        if query is not None:
            all_persons = objects.filter(Q(pid__icontains=query) | Q(name__icontains=query))
    paginator = Paginator(all_persons, 7)
    page = request.GET.get('pg')
    all_persons = paginator.get_page(page)

    return render(request, 'persons.html', {'all_persons': all_persons})


@login_required(login_url='/admin/login/')
def issued(request):
    all_books = Books.objects.all()
    all_persons = Person.objects.all()
    all_issued = Issued.objects.all()
    if request.method == "POST":
        form = IssuedBookForm(request.POST or None)
        if form.is_valid():

            form.save()
            messages.success(request, 'Book issued !')
        else:
            print(form.errors)
            messages.error(request, form.errors)

        return redirect('issued')

    elif request.method == "GET":
        query = request.GET.get("q", None)
        objects = Issued.objects.all()
        if query is not None:
            all_issued = objects.filter(Q(pid__pid__icontains=query) | Q(isbn__isbn__icontains=query))

    paginator = Paginator(all_issued, 7)
    page = request.GET.get('pg')
    all_issued = paginator.get_page(page)

    return render(request, 'issued.html',
                  {'all_issued': all_issued, 'all_books': all_books, 'all_persons': all_persons})


@login_required(login_url='/admin/login/')
def delete_book(request, task_id):
    task = Books.objects.get(pk=task_id)
    task.delete()
    messages.success(request, "Record Deleted!")
    return redirect('books')


@login_required(login_url='/admin/login/')
def delete_person(request, task_id):
    task = Person.objects.get(pk=task_id)
    task.delete()
    messages.success(request, "Record Deleted!")
    return redirect('persons')


@login_required(login_url='/admin/login/')
def delete_issued(request, task_id):
    task = Issued.objects.get(pk=task_id)
    task.delete()
    messages.success(request, "Record Deleted!")
    return redirect('issued')


@login_required(login_url='/admin/login/')
def edit_book(request, task_id):
    if request.method == "POST":
        task = Books.objects.get(pk=task_id)
        form = BookForm(request.POST or None, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book Edited !')
        else:
            messages.error(request, form.errors)
        return redirect('books')
    else:
        task_obj = Books.objects.get(pk=task_id)
        return render(request, 'edit_book.html', {'task_obj': task_obj})


@login_required(login_url='/admin/login/')
def edit_person(request, task_id):
    if request.method == "POST":
        task = Person.objects.get(pk=task_id)
        form = PersonForm(request.POST or None, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Person Edited !')
        else:
            messages.error(request, form.errors)
        return redirect('persons')
    else:
        task_obj = Person.objects.get(pk=task_id)
        return render(request, 'edit_person.html', {'task_obj': task_obj})


@login_required(login_url='/admin/login/')
def edit_issue(request, task_id):
    if request.method == "POST":
        task = Issued.objects.get(pk=task_id)
        data = request.POST.copy()
        pid = data['pid'][-6:].strip()
        isbn = data['isbn'][-10:].strip()
        date = data['expires_on']
        date = datetime.strptime(date, '%Y-%m-%d').date()
        if not date > task.date_issued:
            messages.error(request, 'Expiry Date must be greater than Issued Date')
            return redirect('issued')
        data.update({'pid': pid, 'isbn': isbn, 'expires_on': date})
        form = IssuedBookForm(data or None, instance=task)
        if form.is_valid():

            form.save()
            messages.success(request, 'Issued Book updated !')
        else:
            print(request.POST)
            messages.error(request, form.errors)
        return redirect('issued')
    else:
        task_obj = Issued.objects.get(pk=task_id)
        return render(request, 'edit_issued.html', {'task_obj': task_obj})
