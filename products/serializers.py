from rest_framework import serializers
from .models import Product, Sku
# from products.models import Product

class SkuSerializer(serializers.ModelSerializer):
    markup_percentage = serializers.SerializerMethodField()

    class Meta:
        model = Sku
        fields = ('id', 'size', 'measurement_unit', 'selling_price', 'platform_commission', 'cost_price', 'status', 'markup_percentage')

    def get_markup_percentage(self, obj):
        return obj.markup_percentage
class ProductListSerializer(serializers.ModelSerializer):
    """
    To show list of products.
    """

    class Meta:
        model = Product
        fields = ['id', 'name', 'selling_price', 'description', 'is_refrigerated', 'category']

class ProductDetailSerializer(serializers.ModelSerializer):
    skus = SkuSerializer(many = True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'selling_price', 'description', 'is_refrigerated', 'category', 'managed_by', 'skus')
