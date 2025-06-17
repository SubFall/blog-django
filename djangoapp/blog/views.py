from django.shortcuts import render
from django.core.paginator import Paginator
from blog.models import Post, Page
from django.db.models import Q

QTDE_PASGE = 9

def index(request):
    post_list = Post.objects.get_published()
    paginator = Paginator(post_list, QTDE_PASGE)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(
        request,
        'blog/pages/index.html',
        {'page_obj': page_obj}
    )

def created_by(request, author_pk):
    post_list = Post.objects.get_published().filter(created_by__pk=author_pk)
    paginator = Paginator(post_list, QTDE_PASGE)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(
        request,
        'blog/pages/index.html',
        {'page_obj': page_obj}
    )

def category(request, slug):
    post_list = Post.objects.get_published().filter(category__slug=slug)
    paginator = Paginator(post_list, QTDE_PASGE)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(
        request,
        'blog/pages/index.html',
        {'page_obj': page_obj}
    )

def tag(request, slug):
    post_list = Post.objects.get_published().filter(tags__slug=slug)
    paginator = Paginator(post_list, QTDE_PASGE)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(
        request,
        'blog/pages/index.html',
        {'page_obj': page_obj}
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
    return render(
        request,
        'blog/pages/index.html',
        {
            'page_obj': page_obj,
            'search_value': search_value
        }
    )


def post(request, slug):
    post = Post.objects.filter(slug=slug).first()

    return render(
        request,
        'blog/pages/post.html',
        {'post': post}
    )

def page(request, slug):
    page = Page.objects.filter(slug=slug).filter(is_published=True).first()

    return render(
        request,
        'blog/pages/page.html',
        {'page': page}
    )