from django.urls import path

from app.views import AuthViewSet

urlpatterns = [
    path(
        "login/", AuthViewSet.as_view({"post": "login"})
    ),
    path("register/", AuthViewSet.as_view({"post":"register"})),
]
