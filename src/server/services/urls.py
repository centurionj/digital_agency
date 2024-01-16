from django.urls import path

from server.services.views import ServicesListView

urlpatterns = [
    path('', ServicesListView.as_view(), name='services'),
]
