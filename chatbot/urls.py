from . import views
from django.urls import path


urlpatterns = [
    path('', views.home,name='home'),
    path('past/', views.past,name='past'),
    path('delete_past/<id>', views.delete_past,name='delete_past'),
    
]
