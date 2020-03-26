from rest_framework.exceptions import ParseError
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.mixins import DestroyModelMixin
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework import status

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

class ItemCreateUpdateDelete(DestroyModelMixin, CreateAPIView):
    """
    API endpoint that allows creating, updating and deleting of items.
    """
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAdminUser]

    # overwrite create to return 200 OK instead of 201 created, since sometimes we're updating
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK, headers=headers)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_serializer_context(self):
        return {"pk": self.kwargs['pk']}

class CategoryCreate(CreateAPIView):
    """
    API endpoint that allows creation of a Category.
    """
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]