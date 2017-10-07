from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from googledocs import views

urlpatterns = [
    url(r'^foods$', views.Foods.as_view()),
    url(r'^foods/(?P<id>[0-9]+)$', views.Foods.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
