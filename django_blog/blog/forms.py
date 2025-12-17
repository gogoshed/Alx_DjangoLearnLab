# blog/forms.py
# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User

# class CustomUserCreationForm(UserCreationForm):
#     email = forms.EmailField(required=True, help_text='Required. Enter a valid email address.')

#     class Meta:
#         model = User
#         fields = ("username", "email", "password1", "password2")



from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']


from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write your comment...'}), label='')

    class Meta:
        model = Comment
        fields = ['content']





# blog/forms.py

from django import forms                # <-- MUST be here
from .models import Post, Comment
from taggit.forms import TagWidget      # only if using django-taggit

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']  # include 'tags' if using tagging
        widgets = {
            'tags': TagWidget(),                  # shows tag input in form
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'body']
