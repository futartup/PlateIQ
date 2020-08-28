## PlateIQ

PlateIQ is a company which captures the invoices automatically. It captures handwritten invoices and converts into digital
format. It stores the digitized document in cloud. 

I prefer reading this blog written by my friend:
https://nanonets.com/blog/handwritten-character-recognition/


## Architecture


client -------> Nginx -------> ASGI -------> middlewares --------> view -------> celery task

### Middlewares-

1. First middleware is the token validation middleware
2. Second middleware gives the request a particular ID which also helps in logging any issues related to that particular request.

### celery task

It does the whole thing. It sends the machine learning input file. It uploads the file in database.
It sends email to client. All happens synchronously.

Thanks
