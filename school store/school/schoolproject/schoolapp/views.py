from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect

from schoolapp.models import Category,Product


# Create your views here.
def allProCat(request,c_slug=None):
    c_page=None
    products_list=None
    if c_slug != None:
        c_page=get_object_or_404(Category,slug=c_slug)
        products_list=Product.objects.all().filter(category=c_page,available=True)
    else:
        products_list = Product.objects.all().filter(available=True)

    return render(request, "category.html", {'category': c_page, 'products': products_list})


def proDetail(request,c_slug,product_slug):
    try:
        product=Product.objects.get(category__slug=c_slug,slug=product_slug)
    except  Exception as e:
        raise e
    return render(request,"product.html",{'product':product})

def cse(request):
    return render(request,"cse.html")

def ce(request):
    return render(request,"ce.html")

def me(request):
    return render(request,"me.html")

def ece(request):
    return render(request,"ece.html")

def eee(request):
    return render(request,"eee.html")


def register(request):
    if request.method=='POST':
        username=request.POST['Username']
        password = request.POST['Password']
        password1 = request.POST['Conform password']
        if password==password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return redirect('schoolapp:register')
            else:
                user=User.objects.create_user(username=username,password=password)

                user.save();
                return redirect('schoolapp:login')


        else:
            messages.info(request, "Password not matching")
            return redirect('register')


    return render(request,"register.html")


def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('schoolapp:form')
        else:
            messages.info(request,"invalid username or password")
            return redirect('schoolapp:login')
    return render(request, "login.html")

def form(request):
    return redirect('schoolapp:forms')
    return render(request,'form.html')

def forms(request):
    return render(request,'forms.html')
