import json

from django.forms import model_to_dict
from django.views.generic import View

from interface_app.forms.service_form import ServiceForm
from interface_app.models.service import Service
from interface_app.libs.response import response_failed, response_success, ErrorCode



class BaseDetailView(View):

    # model = Service
    # form = ServiceForm
    # code = ErrorCode.service
    model = None
    form = None
    code = None

    def get(self, request, service_id, *args, **kwargs):
        '''
        获取单个服务
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''
        service = self.model.objects.filter(id=service_id).first()
        if not service:
            return response_failed(code=self.code, message="获取数据失败")

        return response_success(model_to_dict(service))

    def put(self, request, service_id, *args, **kwargs):
        '''
        全量修改单个服务
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''
        body = request.body
        data = json.loads(body, encoding="utf-8")
        form = self.form(data)
        result = form.is_valid()
        if not result:
            return response_failed(message="表单校验失败")
        # service = self.model.objects.filter(id=service_id).update(name=form.cleaned_data['name'], description=form.cleaned_data['description'])
        service = self.model.objects.filter(id=service_id).update(**form.cleaned_data)
        if not service:
            return response_failed(code=self.code.auth, message="获取数据失败")
        return response_success(model_to_dict(service))


    def patch(self, request, service_id, *args, **kwargs):
        '''
        部分修改单个服务
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''
        pass

    def delete(self, request, service_id, *args, **kwargs):
        '''
        删除单个服务
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''
        self.model.objects.filter(id=service_id).delete()
        return response_success("删除成功")