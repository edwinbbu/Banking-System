import django_filters

from transaction.models import Transaction
class TransactionFilter(django_filters.FilterSet):
    class Meta:
        model=Transaction
        fields=['user',]
