from rest_framework import serializers
from .models import (
    TrafficAccidentReport,
    RoadDamageReport,
    PublicTransportIssueReport,
    EnvironmentalHazardReport,
    TrafficFlowIssueReport,
)

class TrafficAccidentReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrafficAccidentReport
        fields = '__all__'

class RoadDamageReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoadDamageReport
        fields = '__all__'

class PublicTransportIssueReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicTransportIssueReport
        fields = '__all__'

class EnvironmentalHazardReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnvironmentalHazardReport
        fields = '__all__'

class TrafficFlowIssueReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrafficFlowIssueReport
        fields = '__all__'
