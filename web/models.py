from django.db import models
from django.urls import reverse
# Create your models here.

class Banner(models.Model):
    title = models.CharField(max_length=200)
    sub_title = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title
    

class Contact(models.Model):
    name = models.CharField(max_length=180)
    email = models.EmailField()
    subject = models.CharField(max_length=180)
    message = models.TextField()
    
    class Meta:
        ordering = ("id",)
        verbose_name_plural = "Contact Form"
    
    def __str__(self):
        return self.name
    
    
class ContactAdress(models.Model):
    email = models.EmailField()
    number = models.CharField(max_length=15)
    place = models.CharField(max_length=100)
    
    def __str__(self):
        return self.email
    
    
class TeamTitle(models.Model):
    title = models.CharField(max_length=180)
    sub_title = models.CharField(max_length=180)
    
    class Meta:
        ordering = ("id",)
        verbose_name_plural = "Team title"
    
    def __str__(self):
        return self.title
    

class Team(models.Model):
    name = models.CharField(max_length=180)
    position = models.CharField(max_length=180)
    image = models.ImageField(upload_to='team/')
    
    class Meta:
        ordering = ("id",)
        verbose_name_plural = "Teams"

    def __str__(self):
        return self.name
    

class FaqTitle(models.Model):
    image = models.ImageField(upload_to='faq/')
    title = models.CharField(max_length=180)
    sub_title = models.CharField(max_length=180)
    
    class Meta:
        ordering = ("id",)
        verbose_name_plural = "Faq title"
    
    def __str__(self):
        return self.title
    

class Faq(models.Model):
    question = models.CharField(max_length=180)
    answer = models.TextField()
    
    def __str__(self):
        return self.question
    
    
class Client(models.Model):
    name = models.CharField(max_length=180)
    image = models.ImageField(upload_to='clients/')
    
    class Meta:
        verbose_name_plural = "Client Logos"
    
    def __str__(self):
        return self.name
    
    
class ProductTitle(models.Model):
    title = models.CharField(max_length=180)
    sub_title = models.CharField(max_length=180)
    
    class Meta:
        ordering = ("id",)
        verbose_name_plural = "Product title"
    
    def __str__(self):
        return self.title
    

class ProductCard(models.Model):
    title = models.CharField(max_length=180)
    sub_title = models.CharField(max_length=180)
    
    def __str__(self):
        return self.title
    
    
class Product(models.Model):
    order = models.IntegerField(unique=True,blank=True,null=True)
    title = models.CharField(max_length=180)
    slug = models.SlugField()
    sub_title = models.CharField(max_length=180,blank=True,null=True)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    icon = models.FileField(upload_to="product_icon/")
    
    class Meta:
        ordering = ("order",)
        verbose_name_plural = "Products"
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("web:product_details", kwargs={"slug": self.slug})
    

class ProductFeature(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    title = models.CharField(max_length=180,blank=True,null=True)
    
    def __str__(self):
        return self.title
    
    
class ProductFeatureSlide(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    icon_image = models.FileField(upload_to="product_feature_icon/",blank=True,null=True)
    title = models.CharField(max_length=180,blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    
    def __str__(self):
        return self.title
    
    
class ServiceTitle(models.Model):
    title = models.CharField(max_length=180)
    sub_title = models.CharField(max_length=180)
    
    class Meta:
        ordering = ("id",)
        verbose_name_plural = "Service Title"
    
    def __str__(self):
        return self.title


class Service(models.Model):
    order = models.IntegerField(unique=True,blank=True,null=True)
    title = models.CharField(max_length=180)
    description = models.TextField()
    image = models.FileField(upload_to='services/')
    
    class Meta:
        ordering = ("order",)
        verbose_name_plural = "Service"
    
    def __str__(self):
        return self.title

    
class TestimonialTitle(models.Model):
    title = models.CharField(max_length=180)
    sub_title = models.CharField(max_length=180)
    
    class Meta:
        ordering = ("id",)
        verbose_name_plural = "Testimonial Title" 
    
    def __str__(self):
        return self.title
    
    
class Testimonial(models.Model):
    name = models.CharField(max_length=180)
    position = models.CharField(max_length=180)
    image = models.ImageField(upload_to='testimonials/')
    description = models.TextField()
    
    def __str__(self):
        return self.name
    

class BranchTitle(models.Model):
    title = models.CharField(max_length=180)
    sub_title = models.CharField(max_length=180)
    
    class Meta:
        ordering = ("id",)
        verbose_name_plural = "Branch Title"
        
    def __str__(self):
        return self.title
    
    
class Branch(models.Model):
    country = models.CharField(max_length=180)
    country_icon = models.FileField(upload_to='branches/')
    name = models.CharField(max_length=180)
    address = models.CharField(max_length=180)
    number = models.CharField(max_length=180)
    image = models.ImageField(upload_to='branches/')
    hover_image = models.ImageField(upload_to='branches/')
    
    class Meta:
        ordering = ("id",)
        verbose_name_plural = "Branches"
    
    def __str__(self):
        return self.name         


class CuttingEdgeProductTitle(models.Model):
    title = models.CharField(max_length=180)
    sub_title = models.CharField(max_length=180)
    
    class Meta:
        ordering = ("id",)
        verbose_name_plural = "Cutting Edge Product Title"
        
    def __str__(self):
        return self.title


class CuttingEdgeProduct(models.Model):
    order = models.IntegerField(blank=True,null=True,unique=True)
    title = models.CharField(max_length=180)
    image = models.ImageField(upload_to='cutting_edge_products/')
    
    class Meta:
        ordering = ("order",)
        verbose_name_plural = "Cutting Edge Products"
    
    def __str__(self):
        return self.title
    

class FeatureTitle(models.Model):
    title = models.CharField(max_length=180)
    sub_title = models.CharField(max_length=180)
    
    class Meta:
        ordering = ("id",)
        verbose_name_plural = "Feature Title" 
    
    def __str__(self):
        return self.title


class Feature(models.Model):
    icon_image = models.FileField(upload_to='features-icon/')
    title = models.CharField(max_length=180)
    description = models.TextField()
    
    class Meta:
        ordering = ("id",)
        verbose_name_plural = "Features" 
    
    def __str__(self):
        return self.title
    

class About(models.Model):
    title = models.CharField(max_length=180,blank=True,null=True)
    description = models.TextField()
    image = models.ImageField(upload_to='about/')
    
    def __str__(self):
        return self.title
    
    
class AboutFeature(models.Model):
    about = models.ForeignKey(About,on_delete=models.CASCADE)
    feature = models.CharField(max_length=180)
    
    def __str__(self):
        return self.feature
    

class Mission(models.Model):
    title = models.CharField(max_length=180)
    description = models.TextField()
    image = models.ImageField(upload_to='mission/')
    
    def __str__(self):
        return self.title
    

class Vision(models.Model):
    title = models.CharField(max_length=180)
    decsription = models.TextField()
    image = models.ImageField(upload_to='vision/')
    
    def __str__(self):
        return self.title
    
    
class Achivement(models.Model):
    title = models.CharField(max_length=180)
    description = models.TextField()
    image = models.FileField(upload_to='achivements/')
    
    class Meta:
        ordering = ("id",)
        verbose_name_plural = "Achivements"
    
    def __str__(self):
        return self.title
    
    
class AchivementFeature(models.Model):
    achivement = models.ForeignKey(Achivement,on_delete=models.CASCADE)
    count = models.CharField(max_length=180,blank=True,null=True)
    title = models.CharField(max_length=180)
    icon = models.FileField(upload_to='achivements/icon',blank=True,null=True)
    
    def __str__(self):
        return self.title
    
    
class Objective(models.Model):
    title = models.CharField(max_length=180)
    description = models.TextField()
    image = models.FileField(upload_to='objectives/')
    
    class Meta:
        ordering = ("id",)
        verbose_name_plural = "Objective"
    
    def __str__(self):
        return self.title
    
    
class ObjectiveFeature(models.Model):
    objective = models.ForeignKey(Objective,on_delete=models.CASCADE)
    title = models.CharField(max_length=180)
    
    def __str__(self):
        return self.title
    
    
class Footer(models.Model):
    title = models.CharField(max_length=180)
    
    def __str__(self):
        return self.title
    
    
class ContactCard(models.Model):
    title = models.CharField(max_length=180)
    description = models.TextField()
    image = models.ImageField(upload_to="conatct/")
    
    class Meta:
        ordering = ("id",)
        verbose_name_plural = "Contact Card"
    
    def __str__(self):
        return self.title
    
    
class Newsletter(models.Model):
    email = models.EmailField()
    
    def __str__(self):
        return self.email

    
class SocialMedia(models.Model):
    social_media = models.CharField(max_length=180)
    link = models.URLField()
    icon = models.CharField(max_length=180)
    
    class Meta:
        ordering = ("id",)
        verbose_name_plural = "Social Medias"
    
    def __str__(self):
        return self.social_media
    