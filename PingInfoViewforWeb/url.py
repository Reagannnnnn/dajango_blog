from django.urls import path
from . import views


app_name = "PingInfoViewforWeb"


urlpatterns = [
    path('PingInfoViewforWeb-index/', views.index, name="PingInfoViewforWeb-index"),
]