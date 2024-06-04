from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import NewsletterForm
from .models import Product, Footer, SocialMedia
def footer_products(request):
    products = Product.objects.all()
    footer = Footer.objects.all().first()
    social_medias = SocialMedia.objects.all()
    newsletter_form = NewsletterForm()

    if request.method == "POST":
        newsletter_form = NewsletterForm(request.POST)
        if newsletter_form.is_valid():
            newsletter_form.save()

    return{
        'footer_products': products,
        'footer': footer,
        'newsletter_form': newsletter_form,
        "social_medias":social_medias
    }