from django.forms import ModelForm
from .models import History
    
class BunnerForm(ModelForm):
    class Meta:
        model = History
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super(BunnerForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            if name == 'metrics' or field =='metrics':
               field.widget.attrs.update({ 'class':'select' })    
            field.widget.attrs.update({ 'class':'form-control form-control-lg bg-dark','placeholder':name, 'id':'form1', })
    
    
