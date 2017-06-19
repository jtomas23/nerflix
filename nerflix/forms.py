# -*- coding: utf-8 -*-
from django.forms import ModelForm
from nerflix.models import Movie
class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ['name','description','anio','category','sort_order']
