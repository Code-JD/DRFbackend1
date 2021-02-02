from django.urls import path
from django.views.generic import TemplateView

app_name = 'kandu'

urlpatterns = [
    path('', TemplateView.as_view(template_name="kandu/index.html")),
]