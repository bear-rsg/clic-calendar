from django import forms
from . import models
from captcha.widgets import ReCaptchaV3
from captcha.fields import ReCaptchaField


class AnswerCreateForm(forms.ModelForm):
    """
    Form to specify fields in the answer create form
    """

    answer_text = forms.CharField(max_length=1000,
                                  widget=forms.Textarea(attrs={'placeholder': 'Answer this month\'s question here'}),
                                  label='Answer the question below')
    name = forms.CharField(label='Name',
                           widget=forms.TextInput(attrs={'placeholder': 'Name (optional)'}))
    captcha = ReCaptchaField(widget=ReCaptchaV3, label='')

    class Meta:
        model = models.Answer
        fields = ('answer_text', 'name', 'question')
