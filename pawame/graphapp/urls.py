from django.conf.urls import url
from graphapp import views

urlpatterns = [
    url(r"^graph$", views.GraphDataView.as_view(), name="graph"),
]