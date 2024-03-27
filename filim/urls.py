from django.urls import path

from.import views

app_name='filim'

urlpatterns = [
     path('', views.index, name="index"),
     path('signup', views.signup, name="signup"),
     path('login', views.user_login, name="login"),
     path('movie/<int:movie_id>/', views.detail, name='detail'),
     path('add/', views.add_movie, name='add_movie'),
     path('update/<int:id>/', views.update, name='update'),
     path('delete/<int:id>/', views.delete, name='delete'),
]