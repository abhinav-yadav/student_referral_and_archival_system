from django.contrib import admin
from django.urls import path,include
from .views import  (
 HomePage,
 about,
 Search,
 Setting,
 ArticleList,
 autoCompleteView,
 searchAutoComplete,
)
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.views.i18n import JavaScriptCatalog


app_name = 'main'

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('about/', about , name = 'about'),
    path('', HomePage.as_view(), name = 'home'),
    path('articles/',include('articles.urls')),
    path('profile/',include('profiles.urls')),

    path('articlelist/', ArticleList.as_view(), name='article_editlist'),
    path('search/', Search.as_view(), name='search'),
    path('settings/', Setting.as_view(), name='setting'),

    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('comments/', include('django_comments_xtd.urls')),
    path(r'jsi18n/', JavaScriptCatalog.as_view(), name='javascript-catalog'),
    path('autocomplete/', autoCompleteView, name='autocomplete'),
    path('search-autocomplete/', searchAutoComplete, name='search-autocomplete'),
    path('hitcount/', include(('hitcount.urls', 'hitcount'), namespace='hitcount')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
