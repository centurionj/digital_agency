from django.urls import path

from server.about.views import AboutView

urlpatterns = [
    path('', AboutView.as_view(), name='about'),
]
