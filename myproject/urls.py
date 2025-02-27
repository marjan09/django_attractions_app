"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path('', views.index, name='index'), 
    path('login/', views.login_view, name='login'),  # Login page
    path('register/', views.register_view, name='register'),  # Register page
    path('logout/', views.logout_view, name='logout'),  # Logout page # Attraction list
    path('attractions/<int:id>/', views.attraction_detail, name='attraction_detail'),  # Individual attraction details
    path('attractions/<int:id>/like/', views.like_attraction, name='like_attraction'), 
    path('attractions/<int:id>/comment/', views.comment_attraction, name='comment_attraction'), 
    path('edit_comment/<int:comment_id>/', views.edit_comment, name='edit_comment'),  # Edit comment
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'), 
    path('search/', views.search_attractions, name='search_attractions'), # Delete comment # Comment on an attraction # Like an attraction

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)