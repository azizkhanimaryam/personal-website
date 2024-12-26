from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('en/home/', views.home, name="home"),  # Added trailing slash
    path('contact/', views.contact_view, name='contact'),
    path('success/', TemplateView.as_view(template_name='success.html'), name='success'),
]


