from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('home', views.home),
    path('about', views.about, name="about"),
    path('mission', views.mission, name="mission"),
    path('edusys', views.edusys, name="edusys"),
    path('associations', views.associations, name="associations"),
    path('clubs', views.clubs, name="clubs"),
    path('achievements', views.achievements, name="achievements"),
    path('alumni2022', views.alumni2022, name="alumni2022"),
    path('news/<int:page>/', views.news, name="news"),
    path('contests/<int:page>/', views.contests, name="contests"),
    path('events/<int:page>/', views.events, name="events"),
    path('<slug:slug>', views.news_details, name="news_details"),
]
