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

    url(r'^tpchNation/$', views.tpchNation_data),

    url(r'^tpchLineitem/$', views.tpchLineitem_data),

    url(r'^tpchOrders/$', views.tpchorder_data),

    url(r'^tpchPart/$', views.tpchpart_data),

    url(r'^tpchPartsupp/$', views.tpchpartsupp_data),

    url(r'^tpchRegion/$', views.tpchregion_data),

    url(r'^tpchSupplier/$', views.tpchsupplier_data),

    url(r'^crashquery/$', views.crashquery),

    url(r'^DBLPquery/$', views.dblpquery),

    url(r'^ssbquery/$', views.ssbquery),

    url(r'^tpchquery/$', views.tpchquery),

    url(r'^world-2query/$', views.worldquery),

    url(r'^seller1/$', views.seller1),

    url(r'^seller2/$', views.seller2),

    url(r'^test/$', views.test),

    url(r'^new_crash/$', views.newCrashData)

]