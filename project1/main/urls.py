from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path('about-us',views.about, name = 'about'),
    path('create',views.create, name = 'create'),
    path('login', views.loginPage, name = 'login' ),
    path('register', views.registerPage, name = 'register'),
    path('logout', views.logoutUser, name = 'logout' ),
    path('project/<str:pk>/', views.project, name="project"),
    path('update/<str:pk>/',views.updateProject, name = 'update'),
    path('delete/<str:pk>/',views.deleteProject, name = 'delete')
]
