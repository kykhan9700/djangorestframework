from django.urls import include, path
from . import views


# Wire up our API using automatic URL routing for fizzbuzz application.
urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('fizzbuzz/', views.fizzbuzzList, name="FizzBuzz List"),
    path('fizzbuzz/<int:pk>', views.fizzbuzzDetail, name="FizzBuzz Details"),

]