from django.urls import path
from .views import home, move_customers, restart_lines

urlpatterns = [
    path("", home),
    path("move", move_customers),
    path("restart", restart_lines)
]
