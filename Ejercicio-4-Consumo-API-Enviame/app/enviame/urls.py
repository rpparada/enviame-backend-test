from django.urls import path
from enviame import views

urlpatterns = [
    path('', views.EnvioListView.as_view(), name='envios'),
    path('envios/<slug:slug>/', views.EnvioDetailView.as_view(), name='envio'),
    path('crear', views.CreateEnvioView.as_view(), name='crear'),
]
