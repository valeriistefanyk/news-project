from django import forms
from news.models import News
import re
from django.core.exceptions import ValidationError
from captcha.fields import CaptchaField, CaptchaTextInput


class ContactForm(forms.Form):
    subject = forms.CharField(
        label='Тема', 
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    content = forms.CharField(
        label='Текст', 
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5 })
    )
    captcha = CaptchaField()


class NewsForm(forms.ModelForm):
    class Meta:        
        model = News
        # fields = '__all__'
        fields = ('title', 'content', 'is_published', 'category')
        widgets = {
            'title': forms.TextInput(
                    attrs={'class': 'form-control'}),
            'content': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 5    
                }),
            'category': forms.Select(attrs={
                'class': 'form-control'}),   
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = "(Оберіть категорію)"
        self.fields['content'].required = False
        self.fields['category'].required = True
        # self.fields['field_name'].queryset = Position.objects.all().values_list('id', 'position')

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Назва статті не повинна починатись з цифри')
        return title
