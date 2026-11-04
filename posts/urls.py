from django.urls import path

from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.PostListView.as_view(), name='index'),
    path('create/', views.PostCreateView.as_view(), name='create'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', views.PostUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.PostDeleteView.as_view(), name='delete'),
    path('<int:post_id>/comment/', views.create_comment, name='comment'),
    path('categories/', views.CategoryListView.as_view(), name='categories'),
    path('categories/<int:category_id>/', views.detail_category,
         name='category'),
]
