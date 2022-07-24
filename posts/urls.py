from django.urls import path

from .views import listviev

app_name = "posts"

urlpatterns = [
    path("posts", listviev, name="posts_list"),
]