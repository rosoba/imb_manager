
from django.forms import ModelForm
from .models import Publication

class PublicationForm(ModelForm):
    class Meta:
        model = Publication
        fields = ['author', 'title']