from django import forms
froms .models import Post

class PostForm(forms.Modelform):
  class Meta:
      model = Post
      fields = ('title','body')
