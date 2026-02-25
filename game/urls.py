from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ballot-blitz/', views.ballotBlitz, name='ballot-blitz'),
    path('steady-hand/', views.steadyHand, name='steady-hand'),
]
