
from concurrent.futures import process
from ProductInventory.models import *

from ProductInventory.serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from rest_framework import viewsets,  status






# ProductCreateViewSet
class ProductCreateViewSet(viewsets.ViewSet):
    def list(self, request):
        product=Products.objects.all()
        product_serializer= ProductsSerializer(product,many=True)
        return Response(product_serializer.data, status=status.HTTP_200_OK)

        

    def create(self, request):
        try:
            print(request.data)
            # save into image gallery details serializer
            image_gallery_details_serializer = ImageGalaryDetailsSerializer(data=request.data,context={"request": request})
            image_gallery_details_serializer.is_valid(raise_exception=True)
            image_gallery_details_serializer.save()
            image_galary_details_id = image_gallery_details_serializer.data['image_galary_details_id']
            print("Id" , image_galary_details_id)
            # save hotel details info with image gallery details id into hotel details table

            product_create_list = []
            product_create_detail = {}

            if request.data["name"] != '':
                product_create_detail["name"] = request.data["name"]
            else:
                dict_response = {
                    'error': True,
                    'message': 'Product Name Required',
                }
                return Response(dict_response, status=status.HTTP_200_OK)

            if request.data["meta"] != '':
                product_create_detail["meta"] = request.data["meta"]
            else:
                dict_response = {
                    'error': True,
                    'message': 'Meta Required',
                }
                return Response(dict_response, status=status.HTTP_200_OK)
            
            #------------------------------------------------------------
            # Here is problem
            if request.data["categories"] != '':
                product_create_detail["category"] = request.data["categories"]
            else:
                dict_response = {
                    'error': True,
                    'message': 'category Required',
                }
                return Response(dict_response, status=status.HTTP_200_OK)
            

            if request.data["sub_categories"] != '' :
                product_create_detail["sub_category"] = request.data["sub_categories"]
            else:
                dict_response = {
                    'error': True,
                    'message': 'sub category Required',
                }
                return Response(dict_response, status=status.HTTP_200_OK)

            #--------------------------------------------------------------------


            if request.data["descriptions"] != '':
                product_create_detail["descriptions"] = request.data["descriptions"]
            else:
                dict_response = {
                    'error': True,
                    'message': 'Descriptions Required',
                }
                return Response(dict_response, status=status.HTTP_200_OK)

            if request.data["alter_text"] != '':
                product_create_detail["alter_text"] = request.data["alter_text"]
            else:
                dict_response = {
                    'error': True,
                    'message': 'Alter Text Required',
                }
                return Response(dict_response, status=status.HTTP_200_OK)


            if request.data["slug"] != '':
                product_create_detail["slug"] = request.data["slug"]
            else:
                dict_response = {
                    'error': True,
                    'message': 'slug Required',
                }
                return Response(dict_response, status=status.HTTP_200_OK)

            if request.FILES["feature_image"] != '':
                product_create_detail["feature_image"] = request.FILES["feature_image"]
            else:
                dict_response = {
                    'error': True,
                    'message': 'Image Required',
                }
                return Response(dict_response, status=status.HTTP_200_OK)


            product_create_detail["image_galary_details_id"] = image_galary_details_id
            print('image_galary_details_id = ', product_create_detail['image_galary_details_id'])
            product_create_detail["is_active"] = True
            print('product details = ', product_create_detail)
            product_create_list.append(product_create_detail)
            product_create_serializer = ProductsSerializer(data=product_create_detail, context={"request": request})
            product_create_serializer.is_valid(raise_exception=True)
            product_create_serializer.save()

            print('product details serializer = ', product_create_serializer.data)
            print('image = ', product_create_serializer.data['id'])


            product = Products.objects.filter(id=product_create_serializer.data['id'])
            if len(product) != 0:
                product = product[0]
                product.category = Categories.objects.get(id=int(request.data['categories']))
                product.sub_category = Sub_Categories.objects.get(id=int(request.data['sub_categories']))
                product.image_galary_details_id = ImageGalaryDetails.objects.get(image_galary_details_id=int(image_galary_details_id))
                product.save()
            try:

                images = request.FILES.getlist('image')
                print("get the images", images)
                print("list image" ,list(images) )
                for image in list(images):
                    
                    image_list = []
                    
                    
                    image_detail = {}

                    if image != '':
                        image_detail["Image"] = image
                    else:
                        dict_response = {
                            'error': True,
                            'message': 'Product Multiple image Required',
                        }
                        return Response(dict_response, status=status.HTTP_200_OK)
                    #image_detail["Image"] = image
                    image_detail["image_galary_details_id"] = image_galary_details_id
                    image_list.append(image_detail)
                    serializer = ImageSerializer(data=image_list, many=True, context={"request": request})
                    serializer.is_valid(raise_exception=True)
                    serializer.save()
            except Exception as e:
                print(str(e))

            dict_response = {"error": False, "message": "Product Information Save Successfully"}
            return Response(dict_response, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(str(e))
            dict_response = {"error": True, "message": f"{str(e)} Product Information Not Save.", 'data': ''}
            return Response(dict_response, status=status.HTTP_400_BAD_REQUEST)
