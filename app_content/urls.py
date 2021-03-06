from os import name
from django.urls import path
from .views import Home, PostDetail, CitiesList, CityDetail, PostDelete, PostUpdate, PostCreate
from app_account import views

urlpatterns = [
	path('', Home.as_view(), name="home"),
  path('cities/', CitiesList.as_view(), name="cities_list"),
  path('cities/<int:pk>/', CityDetail.as_view(), name="city_detail"),
  path('cities/<int:pk>/posts/new/', PostCreate.as_view(), name="post_create"),
	path('posts/<int:pk>/', PostDetail.as_view(), name="post_detail"),
  path('posts/<int:pk>/delete/', PostDelete.as_view(), name="post_delete"),
  path('posts/<int:pk>/update/', PostUpdate.as_view(), name="post_update"),
]
