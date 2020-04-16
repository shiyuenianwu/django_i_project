from interface_app.forms.task_form import TaskForm
from interface_app.libs.response import ErrorCode
from interface_app.models.task import Task
from interface_app.views.base.base_list import BaseListView


class TaskListView(BaseListView):
    model = Task
    form = TaskForm
    code = ErrorCode.task