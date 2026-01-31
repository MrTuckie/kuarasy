from django.urls import path

from apps.panel.views import panel_view

urlpatterns = [path("/", panel_view)]
