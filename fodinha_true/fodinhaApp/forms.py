from django.forms import ModelForm
from .models import tmp_user


class user_form(ModelForm):
    class Meta:
        model = tmp_user
        fields = '__all__'  # user fields I want to display
