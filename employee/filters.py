import django_filters
from django.db.models import Q
from django import forms
from transaction.models import Transaction

class TransactionFilter(django_filters.FilterSet):

    date=django_filters.DateFilter(
        label="Date", method="filter_by_date", widget=forms.DateInput(attrs={'class': "tdate"})
    )
    class Meta:
        model=Transaction
        fields=['user','type','transaction_id']

    def filter_by_date(self,queryset,name,value):
        print(value)
        return queryset.filter(
            Q(transaction_time__date=value)
        )