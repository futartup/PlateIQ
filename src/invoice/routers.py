from rest_framework import routers
from .views import *

invoice_routers = routers.SimpleRouter()
invoice_routers.register(r'v1/pdfupload', ProcessPDFViewSet)
