from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    TrafficAccidentReportViewSet,
    RoadDamageReportViewSet,
    PublicTransportIssueReportViewSet,
    EnvironmentalHazardReportViewSet,
    TrafficFlowIssueReportViewSet,
)

router = DefaultRouter()
router.register(r'traffic-accidents', TrafficAccidentReportViewSet, basename='traffic-accident')
router.register(r'road-damages', RoadDamageReportViewSet, basename='road-damage')
router.register(r'public-transport-issues', PublicTransportIssueReportViewSet, basename='public-transport-issue')
router.register(r'environmental-hazards', EnvironmentalHazardReportViewSet, basename='environmental-hazard')
router.register(r'traffic-flow-issues', TrafficFlowIssueReportViewSet, basename='traffic-flow-issue')

urlpatterns = [
    path('api/', include(router.urls)),
]
