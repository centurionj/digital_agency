from django.urls import path

from server.landing.views import LandingView

urlpatterns = [
    path('', LandingView.as_view(), name='landing'),
]
