
from django.urls import path
from blog.views import index, page, post, created_by, category, tag

urlpatterns = [
    path('', index, name='index'),
    path('post/<slug:slug>/', post, name='post'),
    path('page/', page, name='page'),
    path('created_by/<int:author_pk>/', created_by, name='created_by'),
    path('category/<slug:slug>/', category, name='category'),
    path('tag/<slug:slug>/', tag, name='tag'),
]

