from django import forms
from .models import *
from datetime import date
from ckeditor.widgets import CKEditorWidget
from django.urls import reverse_lazy
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit



# Details how the module is presented.
# Uses CKEditor Package to handle the publication's
# features (text editor, file handling and image storing)

class PublicationCreateForm(forms.ModelForm):

    # Crispy Form utilities
    def __init__(self, *args, **kwargs):
        instance = kwargs.get('instance', None)
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = reverse_lazy('request_submit')
        self.helper.form_method = 'GET'

        # If editing an existing instance, set form action accordingly
        if instance:
            self.helper.form_action = reverse_lazy('edit_publication', args=[instance.id])
        else:
            self.helper.form_action = reverse_lazy('request_submit')


    title = forms.CharField(required=True, label='',
                            widget=forms.TextInput(
                                attrs={"placeholder": "Title"}
                            ))

    # Creates the CKEditor Widget
    # No longer requires a separate image_address attribute,
    # it is built into CKEditor
    body_description = forms.CharField(widget=CKEditorWidget(attrs={
                                "placeholder": "Description" ,
                                "class": "Publication-Class-Name" ,
                                "rows": 8 ,
                                "cols": 32
                            }))

    # Auto generates the date
    publication_date = forms.DateField(label=date.today)

    class Meta:
        model = Publication
        fields = [
            'title',
            'body_description',
        ]

        # Testing
        exclude = ['publication_date']

    def clean_publication_title(self, *args, **kwargs):

        title = self.cleaned_data.get("title")

        if not len(title):
            raise forms.ValidationError("Invalid Title")
        
        return title



# Form containing no subscritable attributes
# utilized to render outside of Admin page
class PublicationMeta(forms.ModelForm):

    class Meta:
        model = Publication
        fields = ['title', 'body_description']
        exclude = ['publication_date']