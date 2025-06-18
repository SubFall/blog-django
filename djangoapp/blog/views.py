from django.shortcuts import render
from django.core.paginator import Paginator
from blog.models import Post, Page
from django.db.models import Q
from django.contrib.auth.models import User
from django.http import Http404

QTDE_PASGE = 9

def index(request):
    post_list = Post.objects.get_published()
    paginator = Paginator(post_list, QTDE_PASGE)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(
        request,
        'blog/pages/index.html',
        {
            'page_obj': page_obj,
            'title': 'home - '
        }
    )

def created_by(request, author_pk):
    user = User.objects.filter(pk=author_pk).first()

    if user is None:
        raise Http404()
    
    user_full_name = user.username

    if user.first_name:
        user_full_name = f'{user.first_name} {user.last_name}'

    page_title = f'posts de {user_full_name} - '

    post_list = Post.objects.get_published().filter(created_by__pk=author_pk)   
    paginator = Paginator(post_list, QTDE_PASGE)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(
        request,
        'blog/pages/index.html',
        {
            'page_obj': page_obj,
            'title': page_title
        }
    )

def category(request, slug):
    post_list = Post.objects.get_published().filter(category__slug=slug)
    paginator = Paginator(post_list, QTDE_PASGE)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    if len(page_obj) == 0:
        raise Http404()
    
    page_title = f'{page_obj[0].category.name} - Categoria - '
    return render(
        request,
        'blog/pages/index.html',
        {
            'page_obj': page_obj,
            'title': page_title
        }
    )

def tag(request, slug):
    post_list = Post.objects.get_published().filter(tags__slug=slug)
    paginator = Paginator(post_list, QTDE_PASGE)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if len(page_obj) == 0:
        raise Http404()
    
    page_title = f'{page_obj[0].tags.first().name} - Tags - '

    return render(
        request,
        'blog/pages/index.html',
        {
            'page_obj': page_obj,
            'title': page_title
        }
    )

def search(request):
    search_value = request.GET.get('search', '')
    
    post_list = (Post.objects.get_published()
                .filter(
                    Q(title__icontains=search_value)   |
                    Q(excerpt__icontains=search_value) |
                    Q(content__icontains=search_value) 
                )
            )
    paginator = Paginator(post_list, QTDE_PASGE)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    page_title = f'{search_value[:15]}'
    return render(
        request,
        'blog/pages/index.html',
        {
            'page_obj': page_obj,
            'search_value': search_value,
            'title': page_title
        }
    )


def post(request, slug):
    post = Post.objects.filter(slug=slug).first()

    if post is None:
        raise Http404()

    page_title = f'{post.title} - Post - '

    return render(
        request,
        'blog/pages/post.html',
        {
            'post': post,
            'title': 'home - '
        }
    )

def page(request, slug):
    page = Page.objects.filter(slug=slug).filter(is_published=True).first()

    if page is None:
        raise Http404()

    page_title = f'{page.title} - Página - '

    return render(
        request,
        'blog/pages/page.html',
        {
            'page': page,
            'title': page_title
        }
    )