'''
@Author: your name
@Date: 2020-02-25 17:24:19
@LastEditTime: 2020-03-20 23:53:22
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \test_dev\django_i_project\interface_app\views\user_views.py
'''
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

# Create your views here.
class UserViews:
    @require_http_methods(['POST'])
    def login(self, request, *args, **kwargs):
        pass

    @require_http_methods(['POST'])
    def register(self, request, *args, **kwargs):
        pass

    @require_http_methods(['DELETE'])
    def logout(self, request, *args, **kwargs):
        pass
    
    @require_http_methods(['GET'])
    def get_user_info(self, request, *args, **kwargs):
        pass