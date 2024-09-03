from django.urls import path
from . import views

urlpatterns = [
    path('', views.reviewsOverview, name='reviewsOverview'),
    path('All/', views.review_list_create, name='review-list-create'),
    path('<int:pk>/', views.review_detail, name='review-detail'),
]
