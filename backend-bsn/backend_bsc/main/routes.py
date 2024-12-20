from django.urls import path, include
from rest_framework.routers import DefaultRouter # type: ignore
from . import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Your API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@yourdomain.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)

router = DefaultRouter()
router.register(r'hauberges', views.HaubergeViewSet)
router.register(r'residents', views.ResidentViewSet)
router.register(r'blacklist', views.BlackListViewSet)
router.register(r'reservations', views.ReservationViewSet)
router.register(r'hauberge_residents', views.HaubergeResidentViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
       path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
