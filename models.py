
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django.forms import ModelForm
from django.urls import reverse
from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey
from django.contrib.auth.models import User

# Create your models here.

# test ####################################
class Category(MPTTModel):
    id = models.AutoField(primary_key=True)
    parent = TreeForeignKey('self',blank=True, null=True, related_name='children',on_delete= models.CASCADE)
    name = models.CharField(max_length=50)
    slug = models.SlugField(null=False, unique=True)
    image = models.ImageField(null=True, blank=True)



    def __str__(self):
        return self.name

    class MPTTMeta:


        order_insertion_by = ['name']

    def get_absolute_url(self):
       return reverse('category_detail',kwargs={'slug':self.slug})



class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    cantitate = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    slug = models.SlugField(null=False, unique=True)
    image = models.ImageField(null=True, blank=True)
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=True)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail',kwargs={'slug':self.slug})

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['category','name','image','description','price','status']
        #fields = '__all__'

class Product1Form(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'



class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null=True)
    phone = models.CharField(max_length=200,null=True)
    date_created  = models.DateTimeField(auto_now_add=True)
    address = models.CharField(blank=True, max_length=150)

    def __str__(self):
        #return self.user.username
        return str(self.name)

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1',
                  'password2']


class Order(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,blank=True,null=True)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_ordered = models.DateTimeField(format(['%Y-%m-%d %H:%M']),auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)






    def __str__(self):
        return str(self.customer.user)

    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital == False:
                shipping = True
        return shipping


    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])

        return total

    @property
    def get_cart_total1(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])

        return total

    @property
    def get_cart_total2(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])

        return total








    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])

        return total



class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity =models.IntegerField(default=0,null=True,blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total



class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200,null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address


class Sugestii(models.Model):
    nume = models.CharField(max_length=200, null=True)
    telefon = models.CharField(max_length=15, null=True, blank=True)
    descriere = models.CharField(max_length=500, null=True, blank=True)
    data = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.nume

class sugestiiForm(ModelForm):
    class Meta:
        model = Sugestii
        fields = '__all__'


class Contact(models.Model):
    nume = models.CharField(max_length=200, null=True)
    telefon = models.CharField(max_length=15, null=True, blank=True)
    mesaj = models.CharField(max_length=500, null=True, blank=True)
    data = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.nume

class contactForm(ModelForm):
    class Meta:
        model = Sugestii
        fields = '__all__'

class Email(models.Model):
    nume = models.CharField(max_length=200, null=True)
    telefon = models.CharField(max_length=15, null=True, blank=True)
    data_comanda = models.CharField(max_length=500, null=True, blank=True)
    data = models.DateField(auto_now_add=True)
    email = models.CharField(max_length=200, null=True)


    def __str__(self):
        return self.nume

class emailForm(ModelForm):
    class Meta:
        model = Email
        fields = '__all__'
