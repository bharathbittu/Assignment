from django.db import models
from  django.utils import timezone
# Create your models here.
SENSITIVITY_CHOICES = [("HIGHLY_SENSITIVE", "HIGHLY_SENSITIVE"), ("SENSITIVE", "SENSITIVE"), ("NORMAL", "NORMAL")]
ASSET_TYPES = [("LAPTOP", "LAPTOP"), ("TRAVEL_BAG", "TRAVEL_BAG"), ("PACKAGE", "PACKAGE")]
TRAVEL_TYPES = [("BUS", "BUS"), ("CAR", "CAR"), ("TRAIN", "TRAIN")]
STATUS_TYPES = [("PENDING", "PENDING"), ("EXPIRED", "EXPIRED")]


class requesterData(models.Model):
    requesterId = models.CharField(max_length=20)
    requesterName = models.CharField(max_length=30)
    fromAddress = models.CharField(max_length=100)
    toAddress = models.CharField(max_length=100)
    Date_n_Time = models.DateTimeField(default=timezone.now)
    noOfAssets = models.IntegerField()
    assetSensitivity = models.CharField(max_length=20, choices=SENSITIVITY_CHOICES)
    assetTypes = models.CharField(max_length=20, choices=ASSET_TYPES)
    whomToDeliver = models.CharField(max_length=12)
    #status = models.CharField(max_length=15, choices=STATUS_TYPES)


class riderData(models.Model):
    riderId = models.IntegerField()
    riderName = models.CharField(max_length=30)
    fromAddress = models.CharField(max_length=100)
    toAddress = models.CharField(max_length=100)
    Date_n_Time = models.DateTimeField(max_length=100)
    travelMedium = models.CharField(max_length=30, choices=TRAVEL_TYPES)
    noOfAssets = models.IntegerField()
    status = models.CharField(max_length=15, default='NOT APPLIED')
# share rider transport