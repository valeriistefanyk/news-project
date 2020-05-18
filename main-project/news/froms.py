from django import forms
from news.models import Category, News


class NewsForm(forms.Form):
    title = forms.CharField(max_length=150, label='Назва', widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))
    content = forms.CharField(label='Текст новини', required=False, widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'rows': 5    
        }
    ))
    is_published = forms.BooleanField(label='Опубліковати?', required=False, initial=True)
    category = forms.ModelChoiceField(empty_label='Оберіть катеогрію', label='Категорія', 
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-control'
        })    
    )
