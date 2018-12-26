from django.shortcuts import render, redirect, reverse
from . import models, forms


def hello(request):
    return render(request, 'base.html')


def index(request):
    return render(request, 'login/index.html')


def login(request):
    if request.session.get('is_login', None):
        return redirect(reverse('logins:index'))
    if request.method == 'POST':    # 如果form通过POST方法发送数据
        login_form = forms.UserForm(request.POST)
        message = '请检查填写内容！'
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = models.User.objects.get(name=username)
                if user.password == password:
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.name
                    return redirect(reverse('logins:index'))
                else:
                    message = '密码不正确!'
            except:
                message = '用户名不存在!'
        #return render(request, 'login/login.html', locals())
    else:   # 如果是通过GET方法请求数据，返回一个空的表单
        login_form = forms.UserForm()
    return render(request, 'login/login.html', locals())


def register(request):
    if request.session.get('is_login', None):
        return redirect(reverse('logins:index'))
    if request.method == 'POST':
        register_form = forms.RegisterForm(request.POST)
        message = '请检查填写内容'
        if register_form.is_valid():
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            sex = register_form.cleaned_data['sex']
            if password1 != password2:
                message = '两次密码输入不同！'
                return render(request, 'login/register.html', locals())
            else:
                same_name_user = models.User.objects.filter(name=username)
                if same_name_user:
                    message = '用户已存在，请重新选择用户名！'
                    return render(request, 'login/register.html', locals())

                same_name_email = models.User.objects.filter(email=email)
                if same_name_email:
                    message = '该邮箱已被注册，请使用别的邮箱！'
                    return render(request, 'login/register.html', locals())
                new_user = models.User()
                new_user.name = username
                new_user.password = password1
                new_user.email = email
                new_user.sex = sex
                new_user.save()
                return redirect(reverse('logins:login'))
    register_form = forms.RegisterForm()
    return render(request, 'login/register.html', locals())


def logout(request):
    if not request.session.get('is_login', None):
        return redirect(reverse('logins:index'))
    request.session.flush()
    return redirect(reverse('logins:index'))


