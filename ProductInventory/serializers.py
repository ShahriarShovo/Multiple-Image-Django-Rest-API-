from urllib import response
from rest_framework import serializers
from ProductInventory.models import *




class CategoriesSerializers(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, allow_empty_file=False, allow_null=False, use_url=True, required=False)
    class Meta:
        model = Categories
        fields = "__all__"

class SubCategoriesSerializers(serializers.ModelSerializer):
    category = CategoriesSerializers(many=True)
    #url = serializers.HyperlinkedIdentityField(view_name="Categories:categories-detail")
    image = serializers.ImageField(max_length=None, allow_empty_file=False, allow_null=False, use_url=True, required=False)
    class Meta:
        model = Sub_Categories
        fields = "__all__"




# ImageGalaryDetails serializer
class ImageGalaryDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageGalaryDetails
        fields = '__all__'


# Image serializer

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'



# ProductsSerializer
class ProductsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Products
        fields = '__all__'
        depth=2
        
    def to_representation(self, instance):
        response = super().to_representation(instance)
        # if instance.image_galary_details_id is not None:
        response['image_all'] = ImageSerializer(Image.objects.filter(image_galary_details_id=instance.image_galary_details_id),many=True).data
        return response