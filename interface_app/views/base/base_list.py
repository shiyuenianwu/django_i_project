import json

from django.forms import model_to_dict
from django.views.generic import View


from interface_app.libs.response import response_success, response_failed

class BaseListView(View):

    model = None
    form = None
    code = None

    def get(self, request, *args, **kwargs):
        '''
        获取列表
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''
        service = self.model.objects.all()
        ret = []
        for s in service:
            t = model_to_dict(s)
            ret.append(t)

        return response_success(ret)

    def post(self, request, *args, **kwargs):
        '''
        创建数据
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''
        body = request.body #获取请求数据的身体
        data = json.loads(body, encoding='utf-8') #把请求回来的数据用 loads转换成json
        form = self.form(data) #用formData的方式校验数据是否符合要求
        if not form.is_valid():  #判断校验结果，为空返回错误
            return response_failed()
        # 正确的情况下使用类Service中的object下的create创造这条数据，
        # service = Service.objects.create(name=form.cleaned_data['name'], description=form.cleaned_data['description'])
        service = self.model.objects.create(**form.cleaned_data)
        if not service:
            return response_failed(code=self.code, message="创建服务失败")
        else:
            print(service)
            return response_success(model_to_dict(service))

