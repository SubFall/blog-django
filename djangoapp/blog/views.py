from django.shortcuts import render
from django.core.paginator import Paginator
from blog.models import Post

QTDE_PASGE = 9

def index(request):
    post_list = Post.objects.filter(is_published=True).order_by('-pk')
    paginator = Paginator(post_list, QTDE_PASGE)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(
        request,
        'blog/pages/index.html',
        {'page_obj': page_obj}
    )

def post(request):
    return render(
        request,
        'blog/pages/post.html'
    )

def page(request):
    return render(
        request,
        'blog/pages/page.html'
    )