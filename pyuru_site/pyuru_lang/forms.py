from django import forms

class HelloForm(forms.Form):
    your_name = forms.CharField(
        label='ぴゅる語入力欄',
        max_length=200,
        required=True,
        widget=forms.Textarea()
    )

