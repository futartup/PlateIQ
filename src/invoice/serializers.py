from rest_framework.serializers import ModelSerializer
from invoice.models import *
from rest_framework import serializers


class InvoiceSerializer(ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'