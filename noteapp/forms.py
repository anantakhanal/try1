from django.forms import ModelForm
from .models import NOTES

class NOTESFORM(ModelForm):
    class Meta:
        model=NOTES
        fields =['title', 'description','status', 'priority']