from django.urls import path
from . import views

app_name = 'predictor'

urlpatterns = [
    path('predict/', views.predict_view, name='predict'),
]