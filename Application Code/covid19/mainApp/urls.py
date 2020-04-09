from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('statistics/', views.statistics, name='statistics'),
    path('prevention/', views.prevention, name='prevention'),
    path('faq/', views.faq, name='faq'),
    path('symptoms/', views.symptoms, name='symptoms'),
    path('maps-stats/', views.map_stats, name='map-stats'),
    path('prediction/', views.prediction, name='prediction'),
]
