from django.urls import path
from .views import *

urlpatterns = [
    path('', HelloAuthView.as_view(), name='authiview'),
    path('signup/', UserCreationView.as_view(), name='sign_up')
]
