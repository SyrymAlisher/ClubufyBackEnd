from django.urls import path
from api import views
urlpatterns = [
    path('first/', views.first),
    path('categories/', views.CategoriesView.as_view()),
    path('categories/<int:id>/clubs/', views.clubs_by_category),
    path('clubs/', views.clubs),
]