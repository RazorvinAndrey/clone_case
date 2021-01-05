from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('case', views.CaseListView.as_view()),
    path('case/<int:pk>/', views.CaseDetailView.as_view()),
    path('weapon_line/', views.WeaponLineView.as_view()),
    path('weapon/', views.WeaponListView.as_view()),
    path('weapon/<int:pk>', views.WeaponDetailView.as_view()),
    path('profile/', views.ProfileListView.as_view()),
    path('profile/<int:pk>/', views.ProfileDetailView.as_view()),
]