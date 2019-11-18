from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('^$',views.landing,name='klooniLandingPage'),
    url('^home/',views.home,name='klooniHome'),
    url(r'^search/', views.search_results,name='search_results'),
    ]
if settings.DEBUG:
    urlpatterns
