from django.urls import include, path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
path('signin/', views.signin, name='signin'),
path('signup/', views.signup, name='signup'),
path('signout/',views.signout, name='signout'),
path('follow/<int:num>', views.follow,name='follow'),
path('unfollow/<int:num>', views.unfollow,name='unfollow'),
path('followerss/',views.followerss, name='followerss'),
path('followingss/',views.followingss, name='followingss'),
path('otherprofile/<int:num>',views.otherprofile, name='otherprofile'),
path('addpost/',views.addpost,name='addpost'),
path('allpost/',views.allpost,name='allpost'),
path('like/<int:num>',views.like,name='like'),
path('comments/<int:num>',views.comments,name='comments'),
path('profilepic',views.profilepic,name='profilepic'),
path('<str:username>/',views.profile, name='profile'),
#path('allusers/',views.allusers, name='allusers'),
#path('search_user/',views.search_user, name='search_user'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
