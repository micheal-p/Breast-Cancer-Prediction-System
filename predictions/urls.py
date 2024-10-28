from django.urls import path
from .views import save_prediction

urlpatterns = [
    path('save_prediction/', save_prediction, name='save_prediction'),
]
