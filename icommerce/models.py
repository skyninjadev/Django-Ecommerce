from django.db import models
admin = 'RushX'

# Create your models here.
class Product(models.Model):
    ID_of_the_Product = models.AutoField
    Product_Name = models.CharField(max_length=50)
    Cateogary = models.CharField(max_length=50)
    Price = models.IntegerField(default=0)
    Description = models.TextField(max_length=1000)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='icommerce/images')
    linkToDownload = models.CharField(max_length=500, default='')

    def __str__(self):
        return self.Product_Name

class Order(models.Model):
    country = models.CharField(max_length=20, default='')
    amount = models.CharField(max_length=20)
    itemsJson = models.CharField(max_length=100)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    address = models.CharField(max_length=70)
    state = models.CharField(max_length=20)
    zipcode = models.CharField(max_length=10)
    email = models.CharField(max_length=32)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.firstName

class Contact(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=10000)
    email = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.fname} tried to contact {admin}'