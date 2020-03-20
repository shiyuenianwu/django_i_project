'''
@Author: your name
@Date: 2020-03-20 23:00:23
@LastEditTime: 2020-03-20 23:30:56
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \test_dev\django_i_project\interface_app\libs\reponse.py
'''
from django.http import JsonResponse


class ErrorCode:
    common = 10000


def common_response(success, data, error_code, error_message):

    response = {
        "success": success,
        "data": data,
        "error": {
            "code": error_code,
            "message": error_message
        },
    }

    return JsonResponse(response, safe=False)


def response_success(data={}):
    return common_response(True, data, "", "")


def response_failed(code=ErrorCode.common, message="参数错误", data={}):
    return common_response(False, data, code, message)
