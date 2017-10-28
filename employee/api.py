from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,generics
from customer.models import Customer
from .serializers import CustomerSerializer

class CustomerList(APIView):
    def get(self, request):
        customers=Customer.objects.all()
        s=CustomerSerializer(customers, many=True)
        return Response(s.data)

    def post(self,request):
        pass

class GetCustomer(generics.ListAPIView):
    def get(selfs,request, format=None, *args, **kwargs):
        customer=Customer.objects.get(account_no=request.GET['acc'])
        s=CustomerSerializer(customer)
        return Response(s.data)