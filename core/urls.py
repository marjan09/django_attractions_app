from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Home page
    path('attraction/<int:id>/', views.attraction_detail, name='attraction_detail'),
    path('attraction/<int:id>/like/', views.like_attraction, name='like_attraction'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),  # Login page
    path('logout/', views.logout_view, name='logout'),  # Logout page
    path('attractions/<int:id>/comment/', views.comment_attraction, name='comment_attraction'),  # Comment on an attraction
    path('edit_comment/<int:comment_id>/', views.edit_comment, name='edit_comment'),  # Edit comment
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),  # Delete comment
    path('search/', views.search_attractions, name='search_attractions'),
    path('attraction/add/', views.add_attraction, name='add_attraction'),
    path('edit_attraction/<int:id>/', views.edit_attraction, name='edit_attraction'),
    path('delete_attraction/<int:id>/', views.delete_attraction, name='delete_attraction'),
]