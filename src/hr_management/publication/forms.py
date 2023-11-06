from django import forms
from .models import Publication
from datetime import date
from ckeditor.widgets import CKEditorWidget




# Details how the module is presented.
# Uses CKEditor Package to handle the publication's
# features (text editor, file handling and image storing)

class PublicationCreateForm(forms.ModelForm):

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

    def clean_publication_title(self, *args, **kwargs):

        title = self.cleaned_data.get("title")

        if not len(title):
            raise forms.ValidationError("Invalid Title")
        
        return title
