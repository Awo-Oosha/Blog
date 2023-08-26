from django.urls import path
from . import views


app_name = 'myblog'

urlpatterns = [
    path('blog/', view=views.homeView, name='blog'),
    path('blog/post/<str:slug>/', views.postDetail, name='detail'),
    path('blog/category/<str:name>/', views.categoryDetail, name='category'),
    path('blog/search', views.searchView, name="search")
]