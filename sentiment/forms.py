from django import forms


class SentimentForm(forms.Form):
    sentence = forms.CharField(max_length=255,)
