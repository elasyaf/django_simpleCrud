from django.conf.urls import patterns, url
from crud import views

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^list$', views.CrudList.as_view(), name='crud_list'),
  url(r'^new$', views.CrudCreate.as_view(), name='crud_new'),
  url(r'^edit/(?P<pk>\d+)$', views.CrudUpdate.as_view(), name='crud_edit'),
  url(r'^delete/(?P<pk>\d+)$', views.CrudDelete.as_view(), name='crud_delete'),
]