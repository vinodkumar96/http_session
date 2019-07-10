from django.conf.urls import url
from . import views
app_name="session"
urlpatterns = [
    url(r'^$',views.input),
    url(r'^add$',views.add),
    url(r'^display$',views.display)
]