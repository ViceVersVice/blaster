from django.urls import path

from . import views



urlpatterns = [
    #path("", postList.as_view())

    path("post/<int:num>/del", views.DeletePost.as_view(), name="del_post"),
    path("post/<int:num>/edit", views.EditPost.as_view(), name="edit_post"),
    path("post/id=<int:post_id>/", views.postView.as_view(), name="post1"),
    path("questions_answers/", views.homeTestView.as_view(), name="homeT"),
    path("About/", views.AboutView, name="about"),

    #path("homeT/%3Fpage=<int:num>", views.homeTestView.as_view(), name="actual_page"),
    #path("homeT/?page=<int:num>/post=<int:id>/", views.PostDetailTestView.as_view(), name="post_comments"),
    #path("comment/", views.comment, name="com"),
]
