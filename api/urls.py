from django.urls import path
from api import views
from rest_framework_jwt.views import obtain_jwt_token
urlpatterns = [
    path('first/', views.first),
    path('categories/', views.CategoriesView.as_view()),
    path('categories/<int:id>/clubs/', views.clubs_by_category),
    path('clubs/', views.clubs),
    path('clubs/<int:id>/', views.club),
    path('enroll/', views.EnrollmentView.as_view()),
    path('login/', obtain_jwt_token)
]