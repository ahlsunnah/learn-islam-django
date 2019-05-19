from django import forms
from .widgets import Quiz

class QuizTranslationForm(forms.ModelForm):
    class Meta:
        widgets = {
            'data': Quiz
        }
