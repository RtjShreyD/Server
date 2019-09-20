from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('seriallist', views.SerialNoListView)
router.register('loggerlist', views.LogListView)
router.register('ordercreatestatus', views.OrderCreateStatusSetView)
router.register('orderlist', views.OrderListView)

urlpatterns = [
    path('', include(router.urls))
]