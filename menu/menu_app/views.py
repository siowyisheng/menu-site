from rest_framework.exceptions import ParseError
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response

from .models import Category, MenuItem
from .serializers import CategorySerializer, MenuItemSerializer, MenuItemListSerializer

class ItemsList(ListAPIView):
    """
    API endpoint that shows MenuItems.
    """
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemListSerializer
    permission_classes = [AllowAny]

    def list(self, request, pk=None):
        queryset = self.get_queryset()
        if pk:
            queryset = queryset.filter(category__pk=pk)
        if limit := request.query_params.get('limit'):
            try:
                limit = int(limit)
            except:
                raise ParseError('Limit must be a number.')
            queryset = queryset[:limit]
        serializer = MenuItemListSerializer(queryset, many=True)
        return Response(serializer.data)