from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import redirect, render


# Create your views here.
def index(request):
    context = {}
    return render(request, template_name='index.html', context = context)

def login(request):#หน้าสมัครสมาชิกและล็อกอิน
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

    return render(request, template_name='login.html', context = context)

@login_required
def logoutUser(request):
    logout(request)
    return redirect('login')

def register(request):#หน้าสมัครสมาชิกและล็อกอิน
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
def changepassword(request):#หน้่าสมาชิกเปลี่ยนรหัส
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
    return render(request, 'user.html', context)

def forgotpassword(request):#หน้าลืมรหัสผ่าน
    return render(request, template_name='forgot.html')  
