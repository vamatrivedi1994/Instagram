from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import UserForm, SigninForm, SearchForm, Follower, Posts, Posts_form, Comments, Comments_form
from . models import Profile_photo, profilephoto_form
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.conf import settings
from django.conf.urls.static import static


def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            Username = form.cleaned_data['Username']
            EmailAddress  = form.cleaned_data['EmailAddress']
            FirstName = form.cleaned_data['FirstName']
            LastName = form.cleaned_data['LastName']
            Password = form.cleaned_data['Password']
            a = User.objects.create(username=Username, email= EmailAddress, first_name=FirstName, last_name=LastName)
            a.set_password(form.cleaned_data['Password'])
            a.is_staff = True
            a.is_superuser = True
            a.save()
            return redirect('/instagram/signin')
    else:
        form = UserForm()
    return render(request, "signup.html", {'UserForm': form,})


def signin(request):
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():
            Username = form.cleaned_data['Username']
            Password = form.cleaned_data['Password']
            Username = request.POST.get('Username')
            Password = request.POST.get('Password')
            abc = authenticate(request,username=Username, password=Password)
            if abc is not None:
                login(request, abc)
                return redirect('/instagram/'+Username+'/')
            else:
                return redirect('/instagram/signin/')

    else:
        form = SigninForm()
    return render(request, "signin.html", {'SigninForm': form})

def follow(request,num):
    followed= User.objects.get(id=num)
    current = request.user
    if Follower.objects.filter(follower = current, following = followed).exists():
        Follower.objects.filter(follower = current, following = followed).delete()
        # request.session['button_value']= 'Unfollow'
        return redirect('/instagram/profile/')
    else:
        following=Follower(follower = current, following = followed)
        # request.session['button_value']= 'Follow'
        following.save()
        return redirect('/instagram/profile/')

def profile(request, username):
    username = request.user.username
    a = Profile_photo.objects.filter(user_id = request.user)
    b = User.objects.exclude(username = request.user.username)
    img = Posts.objects.filter(owner = request.user).order_by('date_created').reverse()
    counts = request.user.following.count()
    count_followers = request.user.followers.count()
    count_posts = Posts.objects.filter(owner = request.user).count()
    # v = request.session['button_value']
    return render(request, "profile.html", {'username': request.user.username, 'user': b, 'counts': counts, 'count_followers': count_followers, "img":img, 'media_url':settings.MEDIA_URL, 'profile_pic': a, 'count_posts': count_posts, })

def unfollow(request,num):
    followed= User.objects.get(id=num)
    current = request.user
    Follower.objects.filter(follower = current, following = followed).delete()
    return redirect('/instagram/profile/')

def followerss(request):
    username = request.user.username
    followers=request.user.following.all()
    return render(request, "followerss.html", {'username':username,'Follower':followers })

def followingss(request):
    username = request.user.username
    followings=request.user.followers.all()
    return render(request, "followingss.html", {'username':username,'following':followings })

def otherprofile(request, num):
    username = Follower.objects.filter(id=num)
    return render(request, "otherprofile.html", {'username': username,})

def profilepic(request):
    form = profilephoto_form(request.POST, request.FILES)
    if form.is_valid():
        photo = form.cleaned_data['photo']
        user_id = request.user
        a = Profile_photo.objects.create(user_id = user_id, photo = photo)
        a.save()
        return redirect('/instagram/profile')
    else:
        form = profilephoto_form()
    return render(request, "addprofilephoto.html", {'profilephoto_form': form})


def addpost(request):
    if request.method == 'POST':
        form = Posts_form(request.POST, request.FILES)
        if form.is_valid():
            owner = request.user
            photo  = form.cleaned_data['photo']
            caption = form.cleaned_data['caption']
            a = Posts.objects.create(owner = owner, photo = photo, caption=caption)
            a.save()
            return redirect('/instagram/profile')
    else:
        form = Posts_form()
    return render(request, "addpost.html", {'Posts_form': form})

def allpost(request):
    img = Posts.objects.order_by('date_created').reverse()
    comment = Comments.objects.all()
    return render(request, "allpost.html", {"username":request.user,"img":img, 'media_url':settings.MEDIA_URL, "comment": comment})

def like(request, num):
    like = Posts.objects.get(id = num).likes
    like +=1
    Posts.objects.filter(id=num).update(likes = like)
    return redirect('/instagram/allpost/')

def comments(request,num):
    if request.method == 'POST':
        formm =Comments_form(request.POST)
        if formm.is_valid():
            post = Posts.objects.get(id = num)
            author = request.user
            text = formm.cleaned_data['text']
            a = Comments.objects.create(post = post, author = author, text=text)
            a.save()
            return redirect('/instagram/allpost')
    else:
        formm = Comments_form()
    return render(request, "addcomment.html", {'Comments_form': formm})

def signout(request):
    logout(request)
    return redirect('/instagram/signin/')
# def search_user(request):
#     result = "The user does not exist"
#     if request.method == 'POST':
#         form = SearchForm(request.POST)
#         if form.is_valid():
#             usernamee = form.cleaned_data['Usernamee']
#             if User.objects.exclude(pk=self.instance.pk).filter(username=username).exists():
#                 raise forms.ValidationError(u'Username "%s" is already in use.' % usernamee)
#             return render(request, "searchuser.html", {'usernamee': usernamee})
#     else:
#         form = SearchForm()
#     return render(request, "searchuser.html", {'SearchForm': form})
