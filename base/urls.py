from django.urls import path
from base import views

urlpatterns = [
    path('',views.index_view),
    path('register/',views.register_view),
    path('expenses/',views.expenses_view),
    path('expenses/<str:pk>/',views.expenses_detail),
    path('budget/',views.budget_view),
    path('budget/<str:pk>/',views.budget_details)
]