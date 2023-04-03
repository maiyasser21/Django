from django import forms
from polls.models import Question

class QuestionModelForm(forms.ModelForm):
    class Meta:
        model=Question
        fields=["question_txt","pub_date"]