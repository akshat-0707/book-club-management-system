from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register_view, name="register"),
    path("create", views.club_create, name="create"),
    path("clubs", views.club_list, name="clubs"),
    path('club/<int:club_id>/join/', views.join_club, name='join_club')
]