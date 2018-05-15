from django.urls import path, include
from . import views

urlpatterns = [
    path('create',views.create, name='create'),
    path('<pk>',views.ProductDetailView.as_view(), name='detail'),
    path('<int:product_id>/upvote',views.upvote, name='upvote')
]
