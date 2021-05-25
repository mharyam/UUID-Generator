from django.urls import path

from api.views import UUIDAPIVIEW

urlpatterns = [
    path('get-uuid', UUIDAPIVIEW.as_view()),
]