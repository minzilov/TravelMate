from django.urls import path
from apps import views

urlpatterns = [
    path('',apps.views.home, name='home'),
    path('diary',apps.views.diary, name='diary'),
    path('map',apps.views.map, name='map'),
]