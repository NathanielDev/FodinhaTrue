from django.urls import path
from . import views

urlpatterns = [
    path('fodinhaApp/', views.sample_view, name='appFodinha'),
]
