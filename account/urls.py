from django.urls import path
from . import views


urlpatterns = [
    path('weapon_user/', views.WeaponOfUserListView.as_view()),
    path('weapon_user/<int:pk>/', views.WeaponOfUserDetailView.as_view()),
    path('case_user/', views.CaseOfUserListView.as_view()),
    path('login/', views.ExampleView.as_view()),
]
