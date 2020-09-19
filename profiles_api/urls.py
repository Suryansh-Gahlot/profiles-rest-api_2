from django.urls import path

from profiles_api import views

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
]


# Section - 8 (Video 3)
# created a view for learning purposes
# created a urls.py file in profiles_api
# included the new file to the project level url.py file
# imported the views to urls.py file which is in the app
# map the desired url based on the views
