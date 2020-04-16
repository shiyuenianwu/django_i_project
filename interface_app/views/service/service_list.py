from interface_app.models.service import Service
from interface_app.forms.service_form import ServiceForm
from interface_app.libs.response import ErrorCode
from interface_app.views.base.base_list import BaseListView


class ServiceListView(BaseListView):

    model = Service
    form = ServiceForm
    code = ErrorCode.service