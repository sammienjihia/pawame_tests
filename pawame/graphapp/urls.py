from django.conf.urls import url
from graphapp import views

urlpatterns = [
    url(r"^graph$", views.GraphDataView.as_view(), name="graph"),
    url(r"^generator/$", views.RandomNumberGen.as_view(), name="generator"),
]