from django.conf.urls import url
from sweet_libs_mvc import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^results/$', views.ResultsPageView.as_view()),
    url(r'^poll/$', views.AboutPageView.as_view()),

]
