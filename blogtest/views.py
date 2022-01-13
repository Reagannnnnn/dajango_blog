from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ArticlePost
import markdown
from .forms import ArticlePostForm
from django.contrib.auth.models import User


def index(request):
    return HttpResponse("Hello@!")


def article_list(request):
    articles = ArticlePost.objects.all()
    context = {'articles': articles}
    # print(context)
    return render(request, 'blogtest/list.html', context)
    # return HttpResponse("Hello@!Article")


def article_detail(request, id):
    article = ArticlePost.objects.get(id=id)
    article.body = markdown.markdown(article.body,
                                     extensions=[
                                         'markdown.extensions.extra',
                                         'markdown.extensions.codehilite'
                                     ])
    context = {'article': article}
    return render(request, 'blogtest/detail.html', context)


def article_create(request):
    if request.method == "POST":
        # print("already post")
        article_post_form = ArticlePostForm(data=request.POST)
        # print(article_post_form)
        if article_post_form.is_valid():
            new_article = article_post_form.save(commit=False)
            new_article.author = User.objects.get(id=1)
            # print(new_article.author)
            new_article.save()
            return redirect("blogtest:article_list")
        else:
            return HttpResponse("表单内容有误，请重新填写。")
    else:
        article_post_form = ArticlePostForm
        print(article_post_form)
        context = {'article_post_form': article_post_form}
        # print(context)
        return render(request, 'blogtest/create.html', context)


def article_delete(request, id):
    article = ArticlePost.objects.get(id=id)
    article.delete()
    return redirect('blogtest:article_list')


def article_safe_delete(request, id):
    if request.method == "POST":
        article = ArticlePost.objects.get(id=id)
        article.delete()
        # print(request)
        return redirect('blogtest:article_list')
    else:
        return HttpResponse("仅允许POST请求")


def article_update(request, id):
    article = ArticlePost.objects.get(id=id)
    if request.method == "POST":
        article_post_form = ArticlePostForm(data=request.POST)
        if article_post_form.is_valid():
            article.title = request.POST['title']
            article.body = request.POST['body']
            article.save()
            return redirect('blogtest:article_detail', id=id)
        else:
            return HttpResponse('表单内容有误，请重新填写')
    else:
        article_post_form = ArticlePostForm()
        context = {"article": article, 'article_post_form': article_post_form }
        return render(request, 'blogtest/update.html', context)