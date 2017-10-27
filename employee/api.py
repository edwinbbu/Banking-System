from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from customer.models import Customer
from .serializers import CustomerSerializer

class CustomerList(APIView):
    def get(self, request):
        customers=Customer.objects.all()
        s=CustomerSerializer(customers, many=True)
        print(s)
        return Response(s.data)

    def post(self,request):
        pass

