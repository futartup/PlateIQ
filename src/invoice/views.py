import boto3, uuid
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response
from invoice.models import *
from invoice.serializers import InvoiceSerializer
from rest_framework.permissions import IsAuthenticated
from invoice.tasks import process_pdf

# Create your views here.
class ProcessPDFViewSet(ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    permission_class = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        #Upload the file to S3
        if 'file' in request.FILES:
            """
            Code to upload the file in S3.
            Commenting it out.
            """
            file = request.FILES.get('file')
            # s3 = boto3.resource('s3', config=Config(signature_version='s3v4'))
            # client = boto3.client('s3')
            # PREFIX = '{}business_partner/{}/company_logo'.format(SERVER_ENV,business_partner_id)
            # response = client.list_objects(Bucket=AWS_STORAGE_BUCKET_NAME, Prefix=PREFIX)
            pdf_location = "path-to-pdf in s3 in AWS"

            # Email to be fetched from the User auth model. For now its hard coded.
            email = "anup25111986@gmail.com"
            uuidw = uuid.uuid4()
        
            # Pass the pdf file to the celery task
            process_pdf.delay(pdf_location, email, uuidw)
        return Response({"status": "Success", 
                         "Message": "You will get a notification upon digitized. Till then please visit https://github.com/futartup/S15AB"}, 
                         status=status.HTTP_200_OK)