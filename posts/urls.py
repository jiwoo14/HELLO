from django.urls import path
from . import views

urlpatterns = [
    path('model/', views.ModelsPageView.as_view(), name='model'),
    path('model/post/', views.CreateModelsView.as_view(), name='model_post'),
    path('model/detail/<int:model_id>/', views.detail, name="model_detail"),

    path('model/filter/orient/', views.filter_orient, name="filter_orient"),
    path('model/filter/western/', views.filter_western, name="filter_western"),
    path('model/filter/classic/', views.filter_classic, name="filter_classic"),
    path('model/filter/modern/', views.filter_modern, name="filter_modern"),

    path('photo/', views.PhotoPageView.as_view(), name="photo"),
    path('photo/post/', views.PhotoCreatePostView.as_view(), name="photo_post"),
    path('photo/detail/<int:photo_id>/', views.photo_detail, name="photo_detail"),

    path('photo/filter/orient/', views.photo_filter_orient, name="photo_filter_orient"),
    path('photo/filter/western/', views.photo_filter_western, name="photo_filter_western"),
    path('photo/filter/classic/', views.photo_filter_classic, name="photo_filter_classic"),
    path('photo/filter/modern/', views.photo_filter_modern, name="photo_filter_modern"),


]