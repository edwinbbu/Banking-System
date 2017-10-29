from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, render_to_response, get_object_or_404

# Create your views here.
from bank.decorators import group_required
from customer.models import Customer
from .filters import TransactionFilter
from transaction.models import Transaction


@login_required
@group_required('Employee')
def index(request):
    return render(request,"ehome.html")

@login_required
@group_required('Employee')
def customer(request):
    customers=Customer.objects.all()
    paginator=Paginator(customers,10)
    page=request.GET.get('page')
    try:
        customers=paginator.page(page)
    except PageNotAnInteger:
        customers = paginator.page(1)
    except EmptyPage:
        customers=paginator.page(paginator.num_pages)

    context={
        "customers":customers
    }
    return render(request,'customer.html',context)

@login_required
@group_required('Employee')
def details(request, acc):
    customer=Customer.objects.filter(account_no=acc)
    context = {
        "data": customer
    }
    return render(request,"profile.html",context)

@login_required
@group_required('Employee')
def search(request):
    tlist=Transaction.objects.all()
    tfilter=TransactionFilter(request.GET, queryset=tlist)

    context={
        'filter':tfilter
    }
    return render(request, 'search/tlist.html',context)
