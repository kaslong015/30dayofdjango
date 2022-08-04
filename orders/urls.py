from django.urls import path
from . import views

urlpatterns = [
    # path('', views.HelloOrder.as_view(), name='hello-order'),
    path('', views.OrderCreateListView.as_view(), name="orders"),
    path('<int:order_id>/', views.OrderDetailView.as_view(), name="order_detail"),
    path('update-status/<int:order_id>/', views.UpdateOrderStatus.as_view(), name="update-status"),
    path('user/<int:user_id>/', views.GetUserOrderView.as_view(), name="order_detail"),
    path('user/<int:user_id>/order/<int:order_id>/', views.GetUserDetailOrderView.as_view(), name="order_detail")
]
