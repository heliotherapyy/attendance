from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', 'attendance_book.views.profile'),
    url(r'^$', 'attendance_book.views.list'),
]