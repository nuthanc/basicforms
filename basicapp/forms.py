from django import forms

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)

    botCatcher = forms.CharField(required=False, widget=forms.HiddenInput)

    def clean_botCatcher(self):
        botValue = self.cleaned_data['botCatcher']
        if len(botValue) > 0:
            raise forms.ValidationError("Gotcha bot")
        return botValue