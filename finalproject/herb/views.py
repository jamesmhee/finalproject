from http.client import HTTPResponse
from logging import warning
from tokenize import group
from urllib.request import Request

from django.contrib import messages
from django.contrib.auth import (authenticate, login, logout,
                                 update_session_auth_hash)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from django.contrib.auth.models import Group, User
from django.contrib.messages.api import success
from django.shortcuts import redirect, render
from django.template.context_processors import request

from .forms import CreateUserForm, AddproductForm
from .models import Image, Order_Product, Payment, Product, Promotion


# Create your views here.
def index(request):
    search = request.GET.get('searchbox')
    product_list = Product.objects.filter(name=search)
    if search != '' and search is not None:
        product_list = Product.objects.filter(title__icontains=search, name=search)

    context = {'product':product_list, 'searchbox': search}
    
    return render(request, 'index.html', context=context)

def my_login(request): #หน้าสมัครสมาชิกและล็อกอิน
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.warning(request, 'ชื่อผู้ใช้งาน หรือ รหัสผ่าน ไม่ถูกต้อง หรือ ไม่มีในระบบ')
    
    context = {}

    return render(request, "login.html", context=context)
    
@login_required(login_url='login')
def my_logout(request):
    logout(request)
    return redirect('login')


def my_register(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = UserCreationForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                group = Group.objects.get(name='user')
                user.groups.add(group)               
                messages.success(request, 'สมัครสมาชิกเรียบร้อย')
            else:
                messages.warning(request, 'สมัครสมาชิกไม่สำเร็จ เนื่องจาก Username หรือ Email นี้มีในระบบอยู่แล้ว หรือ รหัสผ่านไม่ตรงตามเงื่อนไข')
                return redirect('register')

    context = {'form':form}
    return render(request, "register.html", context)

@login_required
def change_mypassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'เปลี่ยนรหัสผ่านใหม่เรียบร้อย')
            return redirect('changepassword')
        else:
            messages.warning(request, 'รหัสผ่านปัจจุบันผิด หรือ รหัสไม่ตรงกัน หรือ ไม่ตรงตามเงื่อนไข')
    else:
        form = PasswordChangeForm(request.user)
    context = {'form':form}    
    return render(request, 'changepassword.html', context)

def create_product(request):
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('quanlity') and request.POST.get('price'):
            product=Product()
            product.name = request.POST.get('name')
            product.quanlity = request.POST.get('quanlity')
            product.price = request.POST.get('price')
            product.save()
        return redirect('index')
    else:
        pass
    return render(request, "createproduct.html")