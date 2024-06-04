from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .forms import ContactForm
from .models import Service, Product, ProductFeature, Team, Faq, Testimonial, Client, Branch, CuttingEdgeProduct, Banner, CuttingEdgeProductTitle, ServiceTitle, FeatureTitle, Feature, TestimonialTitle, BranchTitle, About, AboutFeature, TeamTitle, Mission, Vision, FaqTitle, Achivement, AchivementFeature, Objective, ObjectiveFeature, ProductTitle, ProductCard, ContactCard, ContactAdress, ProductFeatureSlide

# Create your views here.

def index(request):
    banner = Banner.objects.all().first()
    testimonial_title = TestimonialTitle.objects.all().first()
    testimonials = Testimonial.objects.all()
    service_title = ServiceTitle.objects.all().first()
    services = Service.objects.all()
    products = Product.objects.all()
    client_logos = Client.objects.all()
    brach_title = BranchTitle.objects.all().first()
    branches = Branch.objects.all()
    product_title = CuttingEdgeProductTitle.objects.all().first()
    cutting_edge_products = CuttingEdgeProduct.objects.all()
    feature_title = FeatureTitle.objects.all().first()
    features = Feature.objects.all()
    achivement = Achivement.objects.all().first()
    achivement_features = AchivementFeature.objects.filter(achivement=achivement)
    objective = Objective.objects.all().first()
    objectives_features = ObjectiveFeature.objects.filter(objective=objective)
    
    
    context = {
        "is_index": True,
        "banner":banner,
        "testimonial_title":testimonial_title,
        "testimonials": testimonials,
        "services": services,
        "products": products,
        "client_logos": client_logos,
        "branches": branches,
        "cutting_edge_products": cutting_edge_products,
        "product_title": product_title,
        "service_title":service_title,
        "feature_title":feature_title,
        "features":features,
        "brach_title":brach_title,
        "achivement":achivement,
        "achivement_features":achivement_features,
        "objective":objective,
        "objectives_features":objectives_features
        
    }
    return render(request, "web/index.html", context)


def about(request):
    teams = Team.objects.all()
    team_title = TeamTitle.objects.all().first()
    faq_title = FaqTitle.objects.all().first()
    faqs = Faq.objects.all()
    about =  About.objects.all().first()
    about_features = AboutFeature.objects.filter(about=about)
    mission = Mission.objects.all().first()
    vision = Vision.objects.all().first()

    context = {
        "is_about": True,
        "team_title":team_title,
        "teams":teams,
        "faqs":faqs,
        "about":about,
        "about_features":about_features,
        "mission":mission,
        "vision":vision,
        "faq_title":faq_title
    }
    return render(request, "web/about.html",context)


def products(request):
    products = Product.objects.all()
    product_title = ProductTitle.objects.all().first()
    product_card = ProductCard.objects.all().first()
    context = {
        "is_products": True,
        "products":products,
        "product_title":product_title,
        "product_card":product_card
    }
    return render(request, "web/products.html",context)


def service(request):
    services = Service.objects.all()
    service_title = ServiceTitle.objects.all().first()
    
    context = {
        "is_service": True,
        "services": services,
        "service_title":service_title
    }
    return render(request, "web/service.html",context)


def contact(request):
    contect_card = ContactCard.objects.all().first()
    contact_adress = ContactAdress.objects.all().first()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            response_data = {
                "is_contact": True,
                "status": "true",
                "title": "Successfully Submitted",
                "message": "Thank You, Our Team Will Contact You Soon",
            }
        else:
            error_messages = {field: form.errors[field][0] for field in form.errors}
            print("Form Validation Error:", error_messages)  # Print the errors
            response_data = {
                "status": "false",
                "title": "Form Validation Error",
                "message": error_messages,
            }
        return JsonResponse(response_data)
    else:
        form = ContactForm()
        context = {"contect_card": contect_card,"contact_adress":contact_adress, "form": form, "is_contact": True}
    return render(request, "web/contact.html",context)


def product_details(request, slug):
    product = get_object_or_404(Product, slug=slug)
    product_feutures = ProductFeature.objects.filter(product=product)
    feature_slide = ProductFeatureSlide.objects.filter(product=product)
    context = {
        "product": product,
        "product_feutures":product_feutures,
        "feature_slide":feature_slide
    }
    return render(request, "web/product-details.html", context)