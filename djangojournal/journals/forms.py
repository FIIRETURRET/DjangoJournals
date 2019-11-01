from django import forms
from .models import Journal


class NewJournalForm(forms.ModelForm):
    journal_entry = forms.CharField(
        widget=forms.Textarea(
            attrs={ "style": "height: 300px",
                    "height": 305,
                    "cols": 100,
                    'placeholder': 'What is on your mind?\n\nThe max length of the text is 10,000'
            }
        ), 
        max_length=10000,
        #help_text='The max length of the text is 10000.',
        
    )

    class Meta:
        model = Journal
        fields = ['title', 'journal_entry']