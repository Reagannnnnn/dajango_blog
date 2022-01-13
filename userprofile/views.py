from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .forms import UserLoginForm, UserRehisterForm
import json

def user_login(request):
    if request.method == "POST":
        user_login_form = UserLoginForm(data=request.POST)
        # print(user_login_form)
        if user_login_form.is_valid():
            data = user_login_form.cleaned_data
            # print(data)
            user = authenticate(username=data['username'], password=data["password"])
            # print("user")
            # print(data['username'])
            # print(data["password"])
            # print(user)
            if user:
                login(request, user)
                return redirect("blogtest:article_list")
            else:
                return HttpResponse(user_login_form)
        else:
            return HttpResponse("账号/密码不合法，请重新输入")
    elif request.method == "GET":
        user_login_form = UserLoginForm()
        context = {"form": user_login_form}
        # print(context)
        return render(request, "userprofile/login.html", context)
    else:
        return HttpResponse("请使用GET或POST请求数据8")


def user_logout(request):
    logout(request)
    return redirect("blogtest:article_list")


def user_register(request):
    if request.method == "POST":
        user_register_form = UserRehisterForm(data=request.POST)
        print(user_register_form)
        if user_register_form.is_valid():
            new_user = user_register_form.save(commit=False)
            new_user.set_password(user_register_form.cleaned_data['password'])
            new_user.save()
            login(request, new_user)
            return redirect('blogtest:article_list')
        else:
            return HttpResponse("注册表单输入有误,请重新输入～")
    elif request.method == "GET":
        user_register_form = UserRehisterForm()
        context = {'form': user_register_form }
        return render(request, "userprofile/register.html", context)
    else:
        return HttpResponse("请使用GET或POST请求数据8")