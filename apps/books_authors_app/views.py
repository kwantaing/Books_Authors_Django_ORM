from django.shortcuts import render, HttpResponse, redirect
from django.contrib.messages import error
from . import models 

# Create your views here.
def index(request):
    context = {
        'Books' : models.Book.objects.all(),
    }
    return render(request,'index.html', context)

def author(request):
    context={
        'Authors':models.Author.objects.all(),
    }
    return render(request,'authors.html', context)

def showbook(request, id):
    to_exclude = [author.id for author in models.Book.objects.get(id=id).authors.all()]
    context={
        'book':models.Book.objects.get(id=id),
        'all_authors':models.Author.objects.exclude(id__in=to_exclude)
    }
    return render(request, 'book.html', context)

def showauthor(request,id):
    to_exclude = [book.id for book in models.Author.objects.get(id=id).books.all()]
    context={
        'author' :models.Author.objects.get(id=id),
        'all_books':models.Book.objects.exclude(id__in=to_exclude)
    }
    print (context)
    return render(request,'author.html', context)

def add_book(request):
    if request.method == "POST":
        print(request.POST)
        models.Book.objects.create(title=request.POST["title"], desc = request.POST["description"])
        return redirect( '/')
def add_author(request):
    if request.method == "POST":
        models.Author.objects.create(first_name=request.POST["first_name"], last_name = request.POST["last_name"], notes = request.POST["notes"])
        return redirect('/authors')

def add_author_to_book(request):
    if request.method == "POST":
        models.Book.objects.get(id=request.POST["book_id"]).authors.add(models.Author.objects.get(id=request.POST["author_id"]))
        return redirect('/view/books/'+str(request.POST["book_id"]))

def add_book_to_author(request):
    if request.method =="POST":
            models.Author.objects.get(id=request.POST["author_id"]).books.add(models.Book.objects.get(id=request.POST["book_id"]))
            return redirect('/view/authors/'+str(request.POST["author_id"]))
