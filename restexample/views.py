from rest_framework import viewsets, filters

from restexample.models import Revenue, Expense, Category, Plan
from restexample.paginations import StandardPagination
from restexample.serializers import RevenueSerializer, ExpenseSerializer, CategorySerializer, PlanSerializer


class RevenueViewSet(viewsets.ModelViewSet):
    queryset = Revenue.objects.all()
    serializer_class = RevenueSerializer
    pagination_class = StandardPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'description',)

class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    pagination_class = StandardPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'description',)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = StandardPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'description',)
    def get_queryset(self):
        queryset = Category.objects.all()
        type = self.request.query_params.get('type', None)
        if type is not None:
            if(type == 'revenue'):
                queryset = queryset.filter(type='r')
            elif(type == 'expense'):
                queryset = queryset.filter(type='e')
        return queryset


class PlanViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
    pagination_class = StandardPagination
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    ordering_fields = ('value', 'date',)
    def get_queryset(self):
        queryset = Plan.objects.all()
        category_id = self.request.query_params.get('category_id', None)
        if category_id is not None:
            queryset = queryset.filter(id=category_id)
        return queryset
