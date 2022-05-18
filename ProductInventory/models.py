
from django.db import models


# Create your models here.


class Categories(models.Model):
    category_name=models.CharField(max_length=100, null=False, blank=False)
    slug=models.CharField(max_length=255, null=False, blank=False)
    image=models.ImageField(upload_to='media', blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category_code=models.CharField(max_length=100, null=True, blank=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.category_name
# Create your models here.
class Sub_Categories(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name='category')
    sub_category_name=models.CharField(max_length=100, null=False, blank=False)
    slug=models.CharField(max_length=255, null=False, blank=False)
    image=models.ImageField(upload_to='media', blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description=models.TextField(max_length=1500, null=True, blank=True)
    is_active = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.sub_category_name


class ImageGalaryDetails(models.Model):
    image_galary_details_id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.image_galary_details_id)


class Image(models.Model):
    image_id = models.AutoField(primary_key=True)
    Image = models.ImageField(upload_to='media/image/%Y/%d/%b')
    created_at = models.DateTimeField(auto_now_add=True)
    image_galary_details_id = models.ForeignKey(ImageGalaryDetails, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.image_galary_details_id)





class Products(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    slug = models.CharField(max_length=250, null=False, blank=False)
    meta = models.TextField(max_length=500, null=True, blank=True)
    image_galary_details_id = models.ForeignKey(ImageGalaryDetails, on_delete=models.CASCADE, null=True, blank=True)
    descriptions = models.TextField(max_length=500, null=True, blank=True)
    alter_text = models.CharField(max_length=100, null=True, blank=True)
    is_active= models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    feature_image=models.ImageField(upload_to='media')
    
    category=models.ForeignKey(Categories,on_delete=models.CASCADE, related_name='categories', null=True)
    sub_category=models.ForeignKey(Sub_Categories,on_delete=models.CASCADE, related_name='sub_categories', null=True)

    def __str__(self):
        return str(self.name)







    
