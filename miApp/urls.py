from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('categoria/<int:categoria_id>/', views.categoria, name='categoria'),
    path('producto/<int:producto_id>/', views.detalle, name='detalle'),
]
