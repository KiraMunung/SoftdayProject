from django import forms
from .models import Lecon, Commentaire, Reponse


class LeconForm(forms.ModelForm):
    class Meta():
        model = Lecon
        fields = (
            'lesson_id',
            'nom',
            'video',
            'fpe',
            'pdf',
            'position'

        )

class ComForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ('corps',)
        labels = {'corps': 'Commentaires'}
        widgets = {
            'corps':forms.Textarea(attrs={
                'class': 'form-control',
                'rows':4,
                'cols':70,
                'placeholder':'Entrez votre commentaire ici.'

            })
        }


class RepForm(forms.ModelForm):
    class Meta:
        model = Reponse
        fields = ('corps',)
        labels = {'corps': 'Reponses'}
        widgets = {
            'corps':forms.Textarea(attrs={
                'class': 'form-control',
                'rows':2,
                'cols':10,
                'placeholder':'Repondez à ce commentaire ici.'

            })
        }