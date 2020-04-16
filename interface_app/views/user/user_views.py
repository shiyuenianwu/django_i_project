from django.contrib.auth import authenticate, login, logout
import json
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

# Create your views here.
from interface_app.forms.user_form import UserForm
from interface_app.libs.response import response_failed, ErrorCode, response_success

@require_http_methods(['POST'])
def loginUser(request, *args, **kwargs):
    print("登录方法")
    """
    登录
    """
    body = request.body
    data = json.loads(body, encoding='utf=8')
    form = UserForm(data)
    result = form.is_valid()
    if not result:
        return response_failed(message="表单校验失败")
    # authenticate()仅仅是验证用户的登录状态,存在返回该对象,反之返回none
    user = authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password"])
    if not user:
        return response_failed(code=ErrorCode.auth, message="登录失败,该用户不存在")
    else:
        login(request, user)  # 登录持久
        return response_success()


@require_http_methods(['POST'])
def register(request, *args, **kwargs):
    print("注册方法")
    """
    注册
    """
    body = request.body
    data = json.loads(body, encoding='utf-8')
    form = UserForm(data)
    result = form.is_valid()
    if not result:
        return response_failed(message="表单校验失败")
    if User.objects.filter(username=form.cleaned_data["username"]).exists():
        return response_failed(code=ErrorCode.auth, message="该用户已存在")
    else:
        user = User.objects.create_user(username=form.cleaned_data["username"],
                                        password=form.cleaned_data["password"])
        if not user:
            return response_failed(message="注册失败")
        else:
            login(request, user)  # 登录持久化
            return response_success({
                "message":"注册成功"
            })


@require_http_methods(['DELETE'])
def logout(request, *args, **kwargs):
    """
    注销
    """
    logout(request)
    return response_success()


@require_http_methods(['GET'])
def get_user_info(request, *args, **kwargs):
    """
   获取已登录的用户信息
   """
    user = request.user
    if not user:
        return response_failed(code=ErrorCode.auth, message="用户未登录")
    if user.is_authenticated:  # 判断用户是否通过校验
        return response_success(
            data={
                "id": user.id,
                "name": user.username
            }
        )
    else:
        return response_failed(code=ErrorCode.auth, message="用户未登录")
