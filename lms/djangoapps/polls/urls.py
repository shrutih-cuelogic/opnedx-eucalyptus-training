from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^view/reference$', views.view_reference, name='view_reference'),
    url(r'^$', views.create_reference, name='create_reference'),
    url(r'^edit/(?P<reference_id>[0-9]+)/$$', views.edit_reference, name='edit_reference'),
    url(r'^delete/(?P<reference_id>[0-9]+)/$$', views.delete_reference, name='delete_reference'),

]
