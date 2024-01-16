from django.urls import path

from server.contacts.views import ContactsView

urlpatterns = [
    path('', ContactsView.as_view(), name='contacts'),
]