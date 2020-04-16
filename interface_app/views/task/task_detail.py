from interface_app.forms.task_form import TaskForm
from interface_app.libs.response import ErrorCode
from interface_app.models.task import Task
from interface_app.views.base.base_detail import BaseDetailView


class TaskDetailView(BaseDetailView):
    model = Task
    form = TaskForm
    code = ErrorCode.task