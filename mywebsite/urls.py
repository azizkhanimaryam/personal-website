"""
URL configuration for mywebsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.shortcuts import redirect
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from homepage.views import set_language


def redirect_to_home(request):
    return redirect('/en/home')  # Or whatever path you want to redirect to

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', redirect_to_home),  # Redirect from root to '/en/home'
    path('set_language/', set_language, name='set_language'),
    path('', include('homepage.urls')),
]

# Now wrap the rest of the URLs with i18n_patterns
urlpatterns += i18n_patterns(
    path('', include('homepage.urls')),  # Include homepage URLs here
)