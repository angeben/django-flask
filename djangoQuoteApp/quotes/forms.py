from django import forms

class QuoteForm(forms.Form):

    content = forms.CharField(
        label = "Quote",
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Introduce the quote',
                'class' : 'form_input_area'
            }
        )
    )

    author = forms.CharField(
        label = "Author",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Author of the quote',
                'class' : 'form_input'
            }
        )
    )

    origin = forms.CharField(
        label = "Source",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Source of the quote',
                'class' : 'form_input'
            }
        )
    )

    public_options = [
        (1, 'Yes'),
        (0, 'No')        
    ]
    public = forms.TypedChoiceField(
        label = "Public",
        choices = public_options
    )

    image = forms.ImageField(required=False)