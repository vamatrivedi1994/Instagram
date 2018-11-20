from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model


User = get_user_model()

class UserForm(forms.Form):
    Username = forms.CharField(label='Username', max_length='200')
    EmailAddress = forms.CharField(label='Email Address')
    FirstName =  forms.CharField(label='First Name')
    LastName = forms.CharField(label='Last Name')
    Password = forms.CharField(widget=forms.PasswordInput)
    widget = { 'Password': forms.PasswordInput(),}

class SigninForm(forms.Form):
    Username = forms.CharField(label='UserName', max_length='200')
    Password = forms.CharField(widget=forms.PasswordInput)
    widget = { 'Password': forms.PasswordInput(),}

class SearchForm(forms.Form):
    Usernamee = forms.CharField(label='Username', max_length='200')


class Follower(models.Model):
    follower = models.ForeignKey(User, related_name='following', on_delete=models.SET_NULL,null=True, )
    following = models.ForeignKey(User, related_name='followers', on_delete=models.SET_NULL,null=True,)

    # class Meta:
    #     unique_together = ('follower', 'following')

    def __unicode__(self):
        return u'%s follows %s' % (self.follower, self.following)


class Posts(models.Model):
    owner = models.ForeignKey(User, related_name='owner', on_delete=models.SET_NULL,null=True,)
    date_created = models.DateTimeField(auto_now_add=True)
    caption = models.CharField(max_length=50, blank=True)
    photo = models.FileField(upload_to='desktop/')
    likes = models.PositiveSmallIntegerField(default=0, blank=True, null=True)

class Posts_form(forms.Form):
    photo = forms.FileField()
    caption = forms.CharField(max_length=50, label = "Caption")

# class Posts_form(ModelForm):
#     class Meta:
#         model = Posts
#         fields = ['photo','caption']

class Comments(models.Model):
    post = models.ForeignKey(Posts, related_name='comments', on_delete=models.SET_NULL,null=True,)
    author = models.ForeignKey(User, related_name='author', on_delete=models.SET_NULL,null=True,)
    text = models.CharField(max_length = 500)

class Comments_form(forms.Form):
    text = forms.CharField(label='Comment', max_length='500')

class Profile_photo(models.Model):
    user_id = models.ForeignKey(User, related_name='user_id', on_delete=models.SET_NULL,null=True,)
    photo = models.FileField(upload_to='desktop/')

class profilephoto_form(forms.Form):
    photo = forms.FileField()
