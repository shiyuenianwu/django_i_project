from django import forms


class TaskForm(forms.Form):
    name =forms.CharField(
        max_length=50,
        min_length=3,
        required=True,
    )
    description = forms.CharField(
        max_length=50,
        min_length=3,
        required=True,
    )