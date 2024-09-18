from django import forms


class RecordAttForm(forms.Form):
    StudentFullName = forms.CharField(label = 'Your full name', max_length = 400)

    def __str__(self):
        return self.StudentFullName
