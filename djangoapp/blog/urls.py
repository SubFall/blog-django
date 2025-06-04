
from django.urls import path
from blog.views import index, page, post

urlpatterns = [
    path('', index, name='index'),
    path('post/', post, name='post'),
    path('page/', page, name='page'),
]

