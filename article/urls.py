from django.conf.urls import url
from .views import IndexView, DetailView_

app_name = 'article'

urlpatterns = [
    url(r"^index/$", view=IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', DetailView_.as_view(), name="detail"),
]