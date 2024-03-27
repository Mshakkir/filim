from django import forms
from .models import Movie,Review


class MovieForm(forms.ModelForm):

    class Meta:
        model=Movie
        fields=['name','desc','year','Img','category','trailer_link']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text', 'rating']