from django.urls import path

from api import views


urlpatterns = [
    path(
        'personal_card/', views.PersonalCardViewSet.as_view(
            {"get": "list", "post": "create"})
    ),
]
