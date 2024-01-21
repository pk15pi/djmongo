
from django.contrib import admin
from django.urls import path, include
from timeSeriesData.views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'ts', TimeSeriesView),

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', include(router.urls)),
    path('api/delete/', delRecords),
    path('api/update/', updateRecords),
]
