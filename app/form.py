from django.forms import ModelForm
from app.models import Maquinas



class MaquinasForm(ModelForm):
    class Meta:
        model = Maquinas
        fields = ['usuario', 'patrimonio', 'sistema']