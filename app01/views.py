from django.shortcuts import render, redirect

from .forms import UserForm
from .forms import RegisterForm
# Create your views here.
from app01 import models

# 注册
def register2(request):
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():  # 获取数据
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            sex = register_form.cleaned_data['sex']
            if password1 != password2:  # 判断两次密码是否相同
                message = "两次输入的密码不同！"
                return render(request, 'register.html', locals())
            else:
                same_name_user = models.User.objects.filter(name=username)
                if same_name_user:  # 用户名唯一
                    message = '用户已经存在，请重新选择用户名！'
                    return render(request, 'register.html', locals())
                same_email_user = models.User.objects.filter(email=email)
                if same_email_user:  # 邮箱地址唯一
                    message = '该邮箱地址已被注册，请使用别的邮箱！'
                    return render(request, 'register.html', locals())
 
                # 当一切都OK的情况下，创建新用户
 
                new_user = models.User.objects.create()
                new_user.name = username
                new_user.password = password1
                new_user.email = email
                new_user.sex = sex
                new_user.save()
                return redirect('/login/')  # 自动跳转到登录页面
    register_form = RegisterForm()

    return render(request, 'register.html', locals())

def register(request):
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():  # 获取数据
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            sex = register_form.cleaned_data['sex']
            if password1 != password2:  # 判断两次密码是否相同
                message = "两次输入的密码不同！"
                return render(request, 'register.html', locals())
            else:
                same_name_user = models.User.objects.filter(name=username)
                if same_name_user:  # 用户名唯一
                    message = '用户已经存在，请重新选择用户名！'
                    return render(request, 'register.html', locals())
                same_email_user = models.User.objects.filter(email=email)
                if same_email_user:  # 邮箱地址唯一
                    message = '该邮箱地址已被注册，请使用别的邮箱！'
                    return render(request, 'register.html', locals())
 
                # 当一切都OK的情况下，创建新用户
 
                new_user = models.User.objects.create()
                new_user.name = username
                new_user.password = password1
                new_user.email = email
                new_user.sex = sex
                new_user.save()
                return redirect('/login/')  # 自动跳转到登录页面
    register_form = RegisterForm()

    return render(request, 'register.html', locals())

def books_shop(request):
    return render(request, 'books_shop.html')

def social_contact(request):
    return render(request, 'social_contact.html')

def customer_serivice(request):
    return render(request,'customer_serivice.html')

def success_question(request):
    return render(request,'success_question.html')

def logout(request):
    return render(request,'logout.html')

def login(request):
    if request.method == "POST":
        login_form = UserForm(request.POST)
        message = "请检查填写的内容！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = models.User.objects.get(name=username)
                if user.password == password:
                    return redirect('/books_shop/')
                else:
                    message = "密码不正确！"
            except:
                message = "用户不存在！"
        return render(request, 'login.html', locals())
 
    login_form = UserForm()
    return render(request, 'login.html', locals())

def login_phone(request):
    return render(request, 'login_phone.html')

# 出版社列表
def publisher_list(request):
    publisher = models.Publisher.objects.all()
    return render(request, 'list_of_publisher.html', {'publisher_list': publisher})


# 添加出版社
def add_publisher(request):
    if request.method == 'POST':
        new_publisher_name = request.POST.get('name')
        models.Publisher.objects.create(name=new_publisher_name)
        return redirect('/publisher_list/')
    return render(request, 'add_publisher.html')


# 删除出版社
def drop_publisher(request):
    drop_id = request.GET.get('id')
    drop_obj = models.Publisher.objects.get(id=drop_id)
    drop_obj.delete()
    return redirect('/publisher_list/')


# 编辑出版社
def edit_publisher(request):
    if request.method == 'POST':
        edit_id = request.GET.get('id')
        edit_obj = models.Publisher.objects.get(id=edit_id)
        new_name = request.POST.get('name')
        edit_obj.name = new_name
        edit_obj.save()
        return redirect('/publisher_list/')

    edit_id = request.GET.get('id')
    edit_obj = models.Publisher.objects.get(id=edit_id)
    return render(request, 'edit_publisher.html', {'publisher': edit_obj})


# 书籍的列表
def book_list(request):
    book = models.Book.objects.all()
    return render(request, 'list_of_book.html', {'book_list': book})


# 添加本书籍
def add_book(request):
    if request.method == 'POST':
        new_book_name = request.POST.get('name')
        publisher_id = request.POST.get('publisher_id')
        models.Book.objects.create(name=new_book_name, publisher_id=publisher_id)
        return redirect('/book_list/')

    res = models.Publisher.objects.all()
    return render(request, 'add_book.html', {'publisher_list': res})


# 删除本书籍
def drop_book(request):
    drop_id = request.GET.get('id')
    drop_obj = models.Book.objects.get(id=drop_id)
    drop_obj.delete()
    return redirect('/book_list/')


# 编辑本书籍
def edit_book(request):
    if request.method == 'POST':
        new_book_name = request.POST.get('name')
        new_publisher_id = request.POST.get('publisher_id')
        edit_id = request.GET.get('id')
        edit_obj = models.Book.objects.get(id=edit_id)
        edit_obj.name = new_book_name
        edit_obj.publisher_id = new_publisher_id
        edit_obj.save()
        return redirect('/book_list/')

    edit_id = request.GET.get('id')
    edit_obj = models.Book.objects.get(id=edit_id)
    all_publisher = models.Publisher.objects.all()
    return render(request, 'edit_book.html', {'book': edit_obj, 'publisher_list': all_publisher})


# 作者的列表
def author_list(request):
    author = models.Author.objects.all()
    return render(request, 'list_of_author.html', {'author_list': author})


# 添加个作者
def add_author(request):
    if request.method == 'POST':
        new_author_name = request.POST.get('name')
        models.Author.objects.create(name=new_author_name)
        return redirect('/author_list/')
    return render(request, 'add_author.html')


# 删除个作者
def drop_author(request):
    drop_id = request.GET.get('id')
    drop_obj = models.Author.objects.get(id=drop_id)
    drop_obj.delete()
    return redirect('/author_list/')


# 修改下作者
def edit_author(request):
    if request.method == 'POST':
        edit_id = request.GET.get('id')
        edit_obj = models.Author.objects.get(id=edit_id)
        new_author_name = request.POST.get('name')
        new_book_id = request.POST.getlist('book_id')
        edit_obj.name = new_author_name
        edit_obj.book.set(new_book_id)
        edit_obj.save()
        return redirect('/author_list/')

    edit_id = request.GET.get('id')
    edit_obj = models.Author.objects.get(id=edit_id)
    all_book = models.Book.objects.all()
    return render(request, 'edit_author.html', {
        'author': edit_obj,
        'book_list': all_book
    })

