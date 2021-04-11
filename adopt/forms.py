from django.forms import ModelForm
from .models import AdoptRequest


class SquirrelMap(ModelForm):
    class Meta:
        model = SquirrelMap
        fields = [
                'squirrel'
                ]


