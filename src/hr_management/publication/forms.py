from django import forms
from .models import Publication
from datetime import datetime


class PublicationCreateForm(forms.ModelForm):

    title = forms.CharField(required=True, label='',
                            widget=forms.TextInput(
                                attrs={"placeholder": "Title"}
                            )
                            )

    body_description = forms.CharField(
                            widget=forms.Textarea(attrs={
                                "placeholder": "Description" ,
                                "class": "Publication-Class-Name" ,
                                "rows": 8 ,
                                "cols": 32
                            })
                            )
    
    class Meta:
        model = Publication
        fields = [
            'title',
            'body_description',
        ]


        def clean_publication_title(self, *args, **kwargs):

            title = self.cleaned_data.get("title")

            if not len(title):
                raise forms.ValidationError("Invalid Title")
            
            return title
        

        def generate_date():
            return str(datetime.today().strftime('%Y-%m-%d'))