from .models import Category, MenuItem
from rest_framework import serializers


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['name', 'item_id', 'category', 'description', 'thumbnail']

    def create(self, validated_data):
        pk = self.context.get('pk')
        item, _ = MenuItem.objects.update_or_create(pk=pk,
                                                    defaults=validated_data)
        return item


class MenuItemListSerializer(MenuItemSerializer):
    category = serializers.StringRelatedField()


class CategorySerializer(serializers.ModelSerializer):
    items = MenuItemSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['name', 'items']