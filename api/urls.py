from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('seriallist', views.SerialNoListView)
router.register('ordercreatestatus', views.OrderCreateView)
router.register('statusview', views.StatusView)
router.register('userlist', views.UsersListView)

urlpatterns = [
    path('', include(router.urls))
]