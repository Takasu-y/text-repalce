from django import forms
from django.core.exceptions import ValidationError

widgets_textarea = forms.Textarea(
    attrs={
        "class": "form-control",
    }
)

widgets_input = forms.TextInput(
    attrs={
        "class": "form-control",
    }
)

class TextForm(forms.Form):
    text = forms.CharField(label="入力", widget=widgets_textarea)
    search = forms.CharField(label="検索", widget=widgets_input)
    replace = forms.CharField(label="置換", widget=widgets_input)

    def clean(self):
        data = super().clean()
        text = data["text"]

        if len(text) <= 5:
            raise ValidationError("文字数が短すぎます。６文字以上にしてください")

        return data