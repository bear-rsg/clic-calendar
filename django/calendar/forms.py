from django import forms
from . import models
from captcha.fields import ReCaptchaField, ReCaptchaV3


class AnswerCreateForm(forms.ModelForm):
    """
    Form to specify fields in the answer create form
    """

    answer_text = forms.CharField(max_length=1000,
                                  widget=forms.Textarea(attrs={'placeholder': 'Write your answer...'}),
                                  label='Answer the question below')
    captcha = ReCaptchaField(widget=ReCaptchaV3, label='')

    class Meta:
        model = models.Answer
        fields = ('answer_text', 'question')
