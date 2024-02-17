from django.shortcuts import render,redirect
from django.urls import reverse

# Create your views here.
from .models import BOOKS


def home(req):
    data = BOOKS.objects.all()
    print("data", data)
    return render(req, 'index.html' , {"data" : data})

def view_books(req,id):
    data = BOOKS.objects.get(id=id)
    return render(req, 'view.html' , {"book" : data})

def create(req):
    if req.method == "POST":
        book_image = req.POST.get("book_image")
        book_title = req.POST.get("book_title")
        author_name = req.POST.get("author_name")
        publish = req.POST.get("publish")
        disc = req.POST.get("disc")
        BOOKS.objects.create(book_image=book_image,book_title=book_title,author_name=author_name,disc=disc)
        return redirect("home")   
    return render(req, 'create.html')

def update(req,id):
    data = BOOKS.objects.get(id=id)
    return render(req,'update.html',{'book':data})

def update_book(req,id):
    if req.method == "POST":
        post_data = req.POST
        book_image = req.POST.get("book_image")
        book_title = req.POST.get("book_title")
        author_name = req.POST.get("author_name")
        publish = req.POST.get("publish")
        disc = req.POST.get("disc")
        id = req.POST.get("id")
        BOOKS.objects.update(book_image=book_image,book_title=book_title,author_name=author_name,disc=disc)
        print("book",id)
        return redirect("home")
    

def delete(req,id):
    data = get_object_or_404(BOOKS)
    BOOKS.objects.filter(id=id).delete()
    return redirect('home')