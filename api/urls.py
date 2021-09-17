from django.urls import path
from .views import analyze_sentence

urlpatterns = [
    path('', analyze_sentence, name='analyze'),
]
