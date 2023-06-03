from django import forms


class MyForm(forms.Form):
    name = forms.CharField(max_length=100)

    def clean_name(self):
        name = self.cleaned_data['name']
        return name
