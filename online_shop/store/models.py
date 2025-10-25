from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField


class UserProfile(AbstractUser):
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(15),
                                                       MaxValueValidator(70)], null=True, blank=True)
    phone_number = PhoneNumberField()
    STATUS_CHOICES = (
        ('gold', 'gold'), #50%
        ('silver', 'silver'),
        ('bronze', 'bronze'),
        ('simple', 'simple'),
    )
    status = models.CharField(max_length=32, choices=STATUS_CHOICES, default='simple')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name}-{self.last_name}'


class Category(models.Model):
    category_name = models.CharField(max_length=32)
    category_image = models.ImageField(upload_to='category_image', null=True, blank=True)

    def __str__(self):
        return self.category_name



class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='sub_category')
    subcategory_name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.subcategory_name

class Product(models.Model):
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='products')
    product_name = models.CharField(max_length=32)
    product_price = models.PositiveSmallIntegerField()
    article_number = models.PositiveSmallIntegerField()
    product_type = models.BooleanField(null=True, blank=True)
    description = models.TextField()
    video = models.FileField(upload_to='product_video/', null=True, blank=True)
    created_date= models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.product_name}, {self.product_price}'

    def avg_rating(self):
        ratings = self.reviews.all()
        if ratings.exists():
           return round(sum([i.stars for i in ratings]) / ratings.count(), 1)
        return 0

    def count_people(self):
        ratings = self.reviews.all()
        return ratings.count()

class ProductImage(models.Model):
    product = models.ForeignKey(Product,  on_delete=models.CASCADE, related_name='images')
    images = models.ImageField(upload_to='product_image/', null=True, blank=True)


class Review(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField()
    stars = models.PositiveIntegerField(choices=[(i, str(i)) for i in range(1, 11)], null=True, blank=True)
    comment = models.TextField(null=True, blank=True)





    def __str__(self):
        return f'{self.user}, {self.product}, {self.comment}'


class Cart(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}'

    def get_total_price(self):
        return sum([i.get_total_price() for i in self.items.all()])



class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    quantity = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return f'{self.product}, {self.quantity}'


    def get_total_price(self):
        return self.quantity * self.product.product_price




