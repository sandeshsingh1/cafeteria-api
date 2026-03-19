from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from .models import MenuItem, Order
from .serializers import MenuItemSerializer, OrderSerializer

class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['category', 'name']

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]