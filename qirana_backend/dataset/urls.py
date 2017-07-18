# howdy/urls.py
from django.conf.urls import url

from qirana_backend.dataset import views


urlpatterns = [
   # url(r'^$', views.HomePageView.list()),
    url(r'^datasets/$', views.list),

    url(r'^dblp/$', views.dblp_data ),

    url(r'^crash/$', views.crash_data ),

    url(r'^worldcity/$', views.worldCity_data),

    url(r'^worldcountry/$', views.worldCountry_data),

    url(r'^worldLang/$', views.worldLang_data),

    url(r'^ssbcust/$', views.ssbCust_data),

    url(r'^ssbdw/$', views.ssbCust_data),

    url(r'^ssbpart/$', views.ssbpart_data),

    url(r'^ssbsup/$', views.ssbsup_data),

    url(r'^ssbline/$', views.ssbLine_data),

    url(r'^tpchCust/$', views.tpchCust_data),

    url(r'^tpchNation/$', views.tpchCust_data),

    url(r'^crashquery/$', views.crashquery),

    url(r'^DBLPquery/$', views.dblpquery),

    url(r'^ssbquery/$', views.ssbquery),

    url(r'^world-2query/$', views.worldquery)

]