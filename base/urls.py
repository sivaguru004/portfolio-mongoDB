from django.urls import path
from .views import test, contact_form_submit

urlpatterns = [
    path('', test, name='test'),
    path('contact/submit/', contact_form_submit, name='contact_form_submit'),
]