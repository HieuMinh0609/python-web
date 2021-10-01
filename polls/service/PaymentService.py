from polls.models import Payment
from django.db import connections
cursor = connections['default'].cursor()

def getAllPayment () : 
    return  Payment.objects.all()

