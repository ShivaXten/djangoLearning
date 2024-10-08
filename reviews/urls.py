from django.urls import path
from . import views

urlpatterns = [
    path('', views.reviewsOverview, name='reviewsOverview'),
    path('all/', views.review_list, name='review-list'),
    path('<int:pk>',views.reviewDetail, name="reviewDetail"),
    path('create/<int:product_id>/', views.create_review, name='create-review'),
    path('update/<int:pk>/', views.update_review, name='update-review'),
    path('delete/<int:pk>/', views.delete_review, name='delete-review'),
]
