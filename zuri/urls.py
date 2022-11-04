from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.HelloZuriView.as_view(), name="zuri"),
    path('math/', views.MathView.as_view(), name="math")

]
