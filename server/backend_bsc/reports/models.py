from django.db import models
from django.contrib.auth.models import User

class BaseReport(models.Model):
    REPORT_URGENCY_CHOICES = [
        ("low", "Low"),
        ("medium", "Medium"),
        ("high", "High"),
    ]

    description = models.TextField()
    urgency = models.CharField(max_length=6, choices=REPORT_URGENCY_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="base_reports")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class TrafficAccidentReport(BaseReport):
    SEVERITY_CHOICES = [
        ("minor", "Minor"),
        ("major", "Major"),
        ("fatal", "Fatal"),
    ]

    VEHICLE_TYPE_CHOICES = [
        ("car", "Car"),
        ("truck", "Truck"),
        ("motorcycle", "Motorcycle"),
        ("bicycle", "Bicycle"),
        ("pedestrian", "Pedestrian"),
    ]

    severity = models.CharField(max_length=5, choices=SEVERITY_CHOICES)
    involved_vehicles = models.PositiveIntegerField()
    injuries = models.BooleanField()
    vehicle_types = models.JSONField()

    def __str__(self):
        return f"Traffic Accident ({self.severity})"

class RoadDamageReport(BaseReport):
    DAMAGE_TYPE_CHOICES = [
        ("pothole", "Pothole"),
        ("cracking", "Cracking"),
        ("sinkhole", "Sinkhole"),
        ("other", "Other"),
    ]

    WEATHER_CONDITION_CHOICES = [
        ("dry", "Dry"),
        ("wet", "Wet"),
        ("icy", "Icy"),
        ("snowy", "Snowy"),
    ]

    damage_type = models.CharField(max_length=10, choices=DAMAGE_TYPE_CHOICES)
    damage_size = models.FloatField()
    affected_lanes = models.PositiveIntegerField()
    weather_condition = models.CharField(max_length=5, choices=WEATHER_CONDITION_CHOICES)

    def __str__(self):
        return f"Road Damage ({self.damage_type})"

class PublicTransportIssueReport(BaseReport):
    TRANSPORT_TYPE_CHOICES = [
        ("bus", "Bus"),
        ("train", "Train"),
        ("subway", "Subway"),
        ("other", "Other"),
    ]

    ISSUE_TYPE_CHOICES = [
        ("delay", "Delay"),
        ("cancellation", "Cancellation"),
        ("overcrowding", "Overcrowding"),
        ("maintenance", "Maintenance"),
        ("accessibility", "Accessibility"),
    ]

    transport_type = models.CharField(max_length=10, choices=TRANSPORT_TYPE_CHOICES)
    line_number = models.CharField(max_length=50)
    issue_types = models.JSONField()
    estimated_delay = models.CharField(max_length=50)
    affected_stops = models.JSONField()

    def __str__(self):
        return f"Public Transport Issue ({self.transport_type})"

class EnvironmentalHazardReport(BaseReport):
    HAZARD_TYPE_CHOICES = [
        ("spill", "Spill"),
        ("airPollution", "Air Pollution"),
        ("noise", "Noise"),
        ("wildlife", "Wildlife"),
    ]

    hazard_type = models.CharField(max_length=15, choices=HAZARD_TYPE_CHOICES)
    affected_area = models.FloatField()
    wind_direction = models.PositiveIntegerField()
    evacuation_needed = models.BooleanField()
    estimated_duration = models.JSONField()

    def __str__(self):
        return f"Environmental Hazard ({self.hazard_type})"

class TrafficFlowIssueReport(BaseReport):
    ISSUE_TYPE_CHOICES = [
        ("congestion", "Congestion"),
        ("roadwork", "Roadwork"),
        ("event", "Event"),
        ("signalMalfunction", "Signal Malfunction"),
    ]

    DIRECTION_CHOICES = [
        ("northbound", "Northbound"),
        ("southbound", "Southbound"),
        ("eastbound", "Eastbound"),
        ("westbound", "Westbound"),
    ]

    issue_type = models.CharField(max_length=20, choices=ISSUE_TYPE_CHOICES)
    affected_directions = models.CharField(max_length=15, choices=DIRECTION_CHOICES)
    average_speed = models.FloatField()
    estimated_clear_time = models.CharField(max_length=50)
    alternate_routes = models.JSONField()

    def __str__(self):
        return f"Traffic Flow Issue ({self.issue_type})"
