import logging
from celery.decorators import task
from invoice.models import Invoice
from datetime import datetime

logger = logging.getLogger(__name__)


@task
def process_pdf(file_location_s3, email, uuidw):
    logger.info("PROCESSING FILE")

    # file under process by AI
    # assumed dummy data returned by machine learning process
    # file_details = {"asdfadsf": "asfasd", "asdf": "lop"}
    
    if resp:
        obj = Invoice.objects.create(
            uploaded_by=uuidw,
            pdf_file=file_location_s3,
            status=True,
            text_identified_in_box=file_details,
            total=1.0,
            subtotal=2.0,
            tax=1.2,
            # invoice date will be returned by machine learning  
            invoice_date=datetime.now(),
            # due date will be returned by machine learning 
            due_date=datetime.now,
             # additional date will be returned by machine learning in dict
            additional_found_by_computer_vision=additional,
        )
    
         # SEND EMAIL FINALLY
    else:
        # SEND EMAIL TO STAFF THAT SOME PROBLEM HAS OCCURRED
        pass
    