from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')
router.register('profile', views.UserProfileViewSet)
urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('', include(router.urls))
]


# Section - 8 (Video 3)
# created a view for learning purposes
# created a urls.py file in profiles_api
# included the new file to the project level url.py file
# imported the views to urls.py file which is in the app
# map the desired url based on the views
# did testing
# Creating serializers
