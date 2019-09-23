from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('seriallist', views.SerialNoListView)
router.register('transactionlist', views.TransactionListView)
router.register('ordercreatestatus', views.OrderCreateStatusSetView)
router.register('orderlist', views.OrderListView)
router.register('statusview', views.StatusView)

urlpatterns = [
    path('', include(router.urls))
]