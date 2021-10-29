# Rest_framework
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated,IsAdminUser, IsAuthenticatedOrReadOnly

# product
from ...models import Products
from apps.product.api_product.serializer.product_serializer import Product_serializer



class ProductListAPIView(generics.ListAPIView):
    """This endpoint list all of the available Products from the database"""
    queryset = Products.objects.all()
    serializer_class = Product_serializer
    paginate_by = 10
    permission_classes = [IsAuthenticated]


class ProductCreateAPIView(generics.CreateAPIView):
    """This endpoint allows for creation of a Product"""
    queryset = Products.objects.all()
    serializer_class = Product_serializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class ProductUpdateAPIView(generics.UpdateAPIView):
    """This endpoint allows for updating a specific Products by passing in the id of the Products to update"""
    queryset = Products.objects.all()
    serializer_class = Product_serializer
    permission_classes = [IsAuthenticated, IsAdminUser]



class ProductDestroyAPIView(generics.DestroyAPIView):
    """This endpoint allows for deletion of a specific Products from the database"""
    queryset = Products.objects.all()
    serializer_class = Product_serializer
    permission_classes = [IsAuthenticated, IsAdminUser]



class ProductDetailAPIView(generics.RetrieveAPIView):
    """This endpoint allows for detail of a specific Products from the database"""
    queryset = Products.objects.all()
    serializer_class = Product_serializer
    permission_classes = [IsAuthenticated]

