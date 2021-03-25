from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from .views import ProjectListAndFormView

urlpatterns = [
    url(r'^$', ProjectListAndFormView.as_view(), name='main'),
    url('send_email', csrf_exempt(ProjectListAndFormView.send_email), name='send_email'),

]
