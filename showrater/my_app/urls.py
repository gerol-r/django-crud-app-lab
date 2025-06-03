from django.urls import path
from . import views # Import views to connect routes to view functions

urlpatterns = [
    # defining all app level urls in this list
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('shows/', views.show_index, name='show-index'),
    path('shows/<int:show_id>/', views.show_detail, name='show-detail'),
]

