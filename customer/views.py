from decimal import Decimal
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy

from .forms import CustomerForm
from .models import Customer
from transaction.models import Transaction
# Create your views here.

def index(request):
    if request.user.groups.filter(name='Employee').exists():
        return HttpResponseRedirect(reverse('employee:index'))
    return render(request, "index.html")

@login_required
def register(request):
    user = User.objects.get(username=request.user.username)
    customer = Customer(user=user)
    form=CustomerForm(request.POST or None, instance=customer)
    context = {"customerform": form,
               "form_url": reverse_lazy('customer:register'),
               "type":"register"
               }
    if request.method=="POST":
        #print("success")
        if form.is_valid():
            f=form.save()
            f.account_no=f.acc_no()
            f.save()
            group=get_object_or_404(Group, name='Customer')
            user.groups.add(group)
            return HttpResponseRedirect(reverse('customer:index'))
    return render(request, "register.html", context)

@login_required
def edit(request):
    user = get_object_or_404(User, username=request.user.username)
    customer = get_object_or_404(Customer, user=user)
    form = CustomerForm(request.POST or None, instance=customer)
    context = {"customerform": form,
               "form_url": reverse_lazy('customer:edit'),
               "type":"edit"
               }
    if request.method == "POST":
        # print("success")
        if form.is_valid():
            f = form.save()
            f.account_no = f.acc_no()
            f.save()
            return HttpResponseRedirect(reverse('customer:index'))
    return render(request, "register.html", context)

@login_required
def profile(request):
    user = Customer.objects.filter(user=request.user)
    #print(user)
    context={
        "data":user
    }
    return render(request, 'profile.html', context)

@login_required
def withdraw(request):
    user=Customer.objects.filter(user=request.user)
    #print(user)
    context={
        "set":user
    }
    return render(request, 'withdraw.html', context)

@login_required
def amount(request):
    user=Customer.objects.get(user=request.user)
    t=Transaction(previous_balance=Decimal(user.balance))
    withdraw = request.POST.get('withdraw')
    t.amount=Decimal(withdraw)
    a=user.get_balance(withdraw,1)
    if a==-1:
        messages.error(request, "No Balance!")
    else:
        user.balance=a
    t.current_balance=Decimal(user.balance)
    t.user=request.user
    t.save()
    t.transaction_id = t.get_transaction_id()
    t.type='Withdrawal'
    t.save()
    user.save()
    return HttpResponseRedirect(reverse('customer:profile'))

@login_required
def deposit(request):
    user=Customer.objects.get(user=request.user)
    #print(user.balance)
    context={
        "balance":user.balance
    }
    return render(request, 'deposit.html', context)

@login_required
def amount2(request):
    user = Customer.objects.get(user=request.user)
    t=Transaction(previous_balance=Decimal(user.balance))
    amount= request.POST.get('deposit')
    t.amount = Decimal(amount)
    user.balance=user.get_balance(amount,2)
    t.current_balance = Decimal(user.balance)
    t.user = request.user
    t.save()
    t.transaction_id = t.get_transaction_id()
    t.type='Deposit'
    t.save()
    user.save()
    return HttpResponseRedirect(reverse('customer:profile'))

@login_required
def transfer(request):
    user = Customer.objects.get(user=request.user)
    context = {
        "balance": user.balance
    }
    return render(request, 'transfer.html', context)

@login_required
def result(request):
    user=Customer.objects.get(user=request.user)
    amount=request.POST.get("amount")
    acc=request.POST.get("acc")
    acc=str(acc)
    t = Transaction(previous_balance=Decimal(user.balance))
    t.amount = Decimal(amount)
    user2=Customer.objects.get(account_no=acc)
    u2=User.objects.get(username=user2.user.username)
    print(type(u2))
    amount=Decimal(amount)
    t2 = Transaction(previous_balance=Decimal(user2.balance))
    t2.amount = Decimal(amount)
    a = user.get_balance(amount, 1)
    if a == -1:
        messages.error(request, "No Balance!")
        return HttpResponseRedirect(reverse('customer:profile'))
    else:
        user.balance = a
        user2.balance=user2.get_balance(amount,2)
        user2.save()
        t2.current_balance = Decimal(user2.balance)
        t2.user = u2
        t2.save()
        t2.transaction_id = t2.get_transaction_id()
        t2.type = 'Account Transfer'
        t2.save()
    user.save()
    t.current_balance = Decimal(user.balance)
    t.user = request.user
    t.save()
    t.transaction_id = t.get_transaction_id()
    t.type = 'Account Transfer'
    t.save()
    return HttpResponseRedirect(reverse('customer:profile'))