import uuid
from datetime import datetime
from django.db import models

# Create your models here.
class Invoice(models.Model):
    uploaded_by = models.UUIDField(default=uuid.uuid4, unique=True, blank=False)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, blank=False)
    pdf_file = models.CharField(max_length=300, null=True, blank=True)
    status = models.BooleanField(default=True, null=True, blank=True)    
    time_uploaded = models.DateTimeField(default=datetime.now)
    text_identified_in_box = models.TextField(null=True, blank=True)
    total = models.FloatField(null=True, blank=True)
    subtotal = models.FloatField(null=True, blank=True)
    tax = models.FloatField(null=True, blank=True)
    invoice_date = models.DateTimeField(default=datetime.now)
    due_date = models.DateTimeField(default=datetime.now)
    additional_found_by_computer_vision = models.TextField(null=True, blank=True)

