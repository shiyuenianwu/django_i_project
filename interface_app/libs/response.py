from django.http import JsonResponse


class ErrorCode:
    common = 10000
    auth = 10001
    service = 10002
    task = 10003


def common_response(success, data, error_code, error_message):
    if error_code == "" and error_message == "":
        print("1")
        response = {
            "success": success,
            "data": data,
        }
    else:
        print("2")
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
