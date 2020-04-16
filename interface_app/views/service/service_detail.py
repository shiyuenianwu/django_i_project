from interface_app.forms.service_form import ServiceForm
from interface_app.libs.response import ErrorCode
from interface_app.models.service import Service
from interface_app.views.base.base_detail import BaseDetailView


class ServiceDetailView(BaseDetailView):

    model = Service
    form = ServiceForm
    code = ErrorCode.service