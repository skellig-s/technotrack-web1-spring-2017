# coding: utf-8
from django import forms
from models import Category

class SortFormBlogs(forms.Form):
    sort = forms.ChoiceField(choices=(
        ('title', u'Заголовок'),
        ('rate', u'Рейтинг'),
        ('description', u'Описание'),
        ),
        # initial='title',
        # required=False,

    )
    search = forms.CharField(required=False, initial='blog')
