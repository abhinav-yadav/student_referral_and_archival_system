from django.http import HttpResponse, JsonResponse
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from articles.models import Article
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from taggit.models import Tag
from django.contrib.auth.decorators import login_required
from django.views import View
from django.views.generic.edit import FormView
import json

# class Search1(View):
#     def get(self,request):
#         type = request.GET.get('t')
#         query = request.GET.get('q')
#         if type == 'articles':
#             article = Article.objects.filter(Q(title__icontains = query), Q(publish=True)).order_by("-timestamp")
#             common_tags = Article.tags.most_common()[:4]
#             context = {'articles':article,
#                         'common_tags':common_tags,
#                         'profiles':{},
#             }
#         elif type == 'tags':
#             tag = get_object_or_404(Tag, slug=query)
#             # Filter posts by tag name
#             articles = Article.objects.filter(tags=tag)
#             common_tags = Article.tags.most_common()[:4]
#             context = {
#                 'articles':articles,
#                 'common_tags':common_tags,
#                 'profiles':{},
#             }
#         else:
#             user = User.objects.filter(Q(username__icontains = query))
#             common_tags = Article.tags.most_common()[:4]
#             context = {
#                 'articles':{},
#                 'common_tags':common_tags,
#                 'users':user
#             }
#         return render(request,'searchresult.html', context)

class Search(View):
    def get(self,request):
        query = request.GET.get('q')
        if query[0] == '#':
            query = query[1:]
            tag = get_object_or_404(Tag, slug=query)
            # Filter posts by tag name
            articles = Article.objects.filter(tags=tag)
            common_tags = Article.tags.most_common()[:4]
            context = {
                'articles':articles,
                'common_tags':common_tags,
                'profiles':{},
            }
        elif query[0] == '@':
            query = query[1:]
            user = User.objects.filter(Q(username__icontains = query))
            common_tags = Article.tags.most_common()[:4]
            context = {
                'articles':{},
                'common_tags':common_tags,
                'users':user
            }
        else:
            article = Article.objects.filter(Q(title__icontains = query), Q(publish=True)).order_by("-timestamp")
            common_tags = Article.tags.most_common()[:4]
            context = {'articles':article,
                        'common_tags':common_tags,
                        'profiles':{},
            }
        return render(request,'searchresult.html', context)


class HomePage(View):
    def get(self, request):
        if self.request.user.is_authenticated:
            article = Article.objects.filter(publish=True).order_by("-timestamp")
            paginator = Paginator(article, 30)
            page = request.GET.get('page')
            article = paginator.get_page(page)

            common_tags = Article.tags.most_common()[:4]
            context = {'articles':article,
                        'common_tags':common_tags,
            }
            return render(request,'homepage.html', context)
        else:
            return render(request,'index.html')

class Setting(View):
    def get(self, request):
        if self.request.user.is_authenticated:
            return render(request,'settings.html')
        else:
            return redirect('account_login')


class ArticleList(View):
    def get(self, request):
        user = request.user
        articles = Article.objects.filter(author = user).order_by('-timestamp')
        paginator = Paginator(articles, 5)
        page = request.GET.get('page')
        articles = paginator.get_page(page)
        context = {
            'articles' : articles,
        }
        return render(request, 'editlist.html', context)

def about(request):
    return render(request,'about.html')


def autoCompleteView(request):
    if 'term' in request.GET:
        term=request.GET.get('term')
        qs = User.objects.filter(username__icontains=term)
        users = []
        if qs:
            for user in qs:
                users.append(user.username)
        else:
            s='username not found'
            users.append(s)
        return JsonResponse(users, safe=False)

def searchAutoComplete(request):
    if 'term' in request.GET:
        term=request.GET.get('term')
        if term[0]=='#':
            qs = Tag.objects.filter(Q(name__icontains = term[1:]))
            q = []
            if len(qs)>5:
                for _ in range(5):
                    q.append('#'+qs[_].name)
            else:
                for _ in qs:
                    q.append('#'+_.name)

        elif term[0]=='@':
            qs = User.objects.filter(Q(username__icontains = term[1:]))
            q = []
            if len(qs)>5:
                for _ in range(5):
                    q.append('@'+qs[_].username)
            else:
                for _ in qs:
                    q.append('@'+_.username)

        else:
            qs = Article.objects.filter(Q(title__icontains = term), Q(publish=True)).order_by("-timestamp")
            # sort by the no.of views and the likes
            q = []
            if len(qs)>5:
                for _ in range(5):
                    q.append(qs[_].title)
            else:
                for _ in qs:
                    q.append(_.title)

        return JsonResponse(q[:5], safe=False)
