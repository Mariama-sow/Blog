from django import forms
from .models import Articles , Comment
# class ArticlesForm(forms.Form) :
#     title = forms.CharField(min_length=2 , max_length=255)
#     sumary = forms.CharField(min_length=2 , max_length=255 ,required=False)
#     date_pub = forms.DateField(required=False)
#     content = forms.CharField(widget=forms.Textarea(attrs={'required':True}))


class ArticlesForm(forms.ModelForm) :
    cover = forms.ImageField(required=False)

    class Meta:
        model = Articles
        fields = ('title','sumary','date_pub','content','cover')


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('content', )