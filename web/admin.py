from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email','subject',)
    
@admin.register(ContactAdress)
class ContactAdressAdmin(admin.ModelAdmin):
    list_display = ('email',"number","place",)
    
@admin.register(ServiceTitle)
class ServiceTitleAdmin(admin.ModelAdmin):
    list_display = ("title",)
    
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title",)
    
class ProductFeaturesInline(admin.TabularInline):
    model = ProductFeature
    fields = ("title",)
    extra = 1
    
class ProductFeatureSlideInline(admin.TabularInline):
    model = ProductFeatureSlide
    fields = ("title","description","icon_image",)
    extra = 1
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title",)
    prepopulated_fields = {"slug":("title",)}
    inlines = [ProductFeaturesInline,ProductFeatureSlideInline]
    
@admin.register(TeamTitle)
class TeamTitleAdmin(admin.ModelAdmin):
    list_display = ("title","sub_title",)
    
@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("name","position",)
    
@admin.register(FaqTitle)
class FaqTitleAdmin(admin.ModelAdmin):
    list_display = ("title","sub_title",)
    
@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ("question",)
    
@admin.register(TestimonialTitle)
class TestimonialTitleAdmin(admin.ModelAdmin):
    list_display = ("title","sub_title",)
    
@admin.register(Testimonial)
class TestimonailAdmin(admin.ModelAdmin):
    list_display = ("name","position",)
    
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("name",)
    
@admin.register(BranchTitle)
class BranchTitleAdmin(admin.ModelAdmin):
    list_display = ("title","sub_title",)
    
@admin.register(Branch)
class BranchesAdmin(admin.ModelAdmin):
    list_display = ("country","name","number",)
    

@admin.register(CuttingEdgeProductTitle)
class CuttingEdgeProductTitleAdmin(admin.ModelAdmin):
    list_display = ("title", "sub_title",)
    
@admin.register(CuttingEdgeProduct)
class CuttingEdgeProductAdmin(admin.ModelAdmin):
    list_display = ("title",)
    
@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ("title","sub_title",)
    
@admin.register(FeatureTitle)
class FeatureTitleAdmin(admin.ModelAdmin):
    list_display = ("title","sub_title",)
    
@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ("title",)
    
class AboutFeaturesInline(admin.TabularInline):
    model = AboutFeature
    fields = ("feature",)
    extra = 1
    
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ("title",)
    inlines = [AboutFeaturesInline]
    
@admin.register(Mission)
class MissionAdmin(admin.ModelAdmin):
    list_display = ("title",)
    
@admin.register(Vision)
class VisionAdmin(admin.ModelAdmin):
    list_display = ("title",)
    

class AchivementFeaturesInline(admin.TabularInline):
    model = AchivementFeature
    fields = ("title",)
    extra = 1

@admin.register(Achivement)
class AchivementAdmin(admin.ModelAdmin):
    list_display = ("title",)
    inlines = [AchivementFeaturesInline]
    
    
class ObjectiveFeaturesInline(admin.TabularInline):
    model = ObjectiveFeature
    fields = ("title",)
    extra = 1

@admin.register(Objective)
class ObjectiveAdmin(admin.ModelAdmin):
    list_display = ("title",)
    inlines = [ObjectiveFeaturesInline]
    
@admin.register(ProductTitle)
class ProductTitleAdmin(admin.ModelAdmin):
    list_display = ("title",)

@admin.register(ProductCard)
class ProductCardAdmin(admin.ModelAdmin):
    list_display = ("title",)
    
@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):
    list_display = ("title",)
    
@admin.register(ContactCard)
class ContactCardAdmin(admin.ModelAdmin):
    list_display = ("title",)
    
@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ("email",)
    
@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ("social_media",)