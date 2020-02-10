from django.urls import path
from .import views



urlpatterns = [
    path("", views.postviews, name="post"),
    path("post/details/<int:id>/", views.postdetail, name="post_detail"),
]
