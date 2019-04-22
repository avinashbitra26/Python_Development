from django import forms
from django.core import validators


def check_for_a(value):
        if value[0].lower() != 'a':
            raise forms.ValidationError("Name needs to start with A")


class FormName(forms.Form):
    name = forms.CharField(validators=[check_for_a])
    # name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label="Enter your Email again!")
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        verify_email = all_clean_data['verify_email']
        if email != verify_email:
            raise forms.ValidationError("Make sure Email fields are matched!")
    # botcatcher = forms.CharField(required=False, widget=forms.HiddenInput,
    #                              validators=[validators.MaxLengthValidator(0)])
    # botcatcher = forms.CharField(required=False, widget=forms.HiddenInput)
    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError("GOTCHA BOT!")
    #     return botcatcher
