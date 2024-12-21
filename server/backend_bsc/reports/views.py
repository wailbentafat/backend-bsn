from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import (
    TrafficAccidentReport,
    RoadDamageReport,
    PublicTransportIssueReport,
    EnvironmentalHazardReport,
    TrafficFlowIssueReport,
)
from .serializers import (
    TrafficAccidentReportSerializer,
    RoadDamageReportSerializer,
    PublicTransportIssueReportSerializer,
    EnvironmentalHazardReportSerializer,
    TrafficFlowIssueReportSerializer,
)

class TrafficAccidentReportViewSet(viewsets.ModelViewSet):
    queryset = TrafficAccidentReport.objects.all()
    serializer_class = TrafficAccidentReportSerializer
    permission_classes = [IsAuthenticated]

class RoadDamageReportViewSet(viewsets.ModelViewSet):
    queryset = RoadDamageReport.objects.all()
    serializer_class = RoadDamageReportSerializer
    permission_classes = [IsAuthenticated]

class PublicTransportIssueReportViewSet(viewsets.ModelViewSet):
    queryset = PublicTransportIssueReport.objects.all()
    serializer_class = PublicTransportIssueReportSerializer
    permission_classes = [IsAuthenticated]

class EnvironmentalHazardReportViewSet(viewsets.ModelViewSet):
    queryset = EnvironmentalHazardReport.objects.all()
    serializer_class = EnvironmentalHazardReportSerializer
    permission_classes = [IsAuthenticated]

class TrafficFlowIssueReportViewSet(viewsets.ModelViewSet):
    queryset = TrafficFlowIssueReport.objects.all()
    serializer_class = TrafficFlowIssueReportSerializer
    permission_classes = [IsAuthenticated]
