from django.shortcuts import render, get_object_or_404

from .models import Product, Service, About, Contacts


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, available=True)
    return render(request, "main/product/detail.html", {"product": product})


def service_detail(request, slug):
    service = get_object_or_404(Service, slug=slug, available=True)
    return render(request, "main/service/detail.html", {"service": service})


def index(request):
    query = request.GET.get("q")
    tab = request.GET.get("tab", "products")
    message = ""

    if tab == "products":
        if query:
            products = Product.objects.filter(name__icontains=query)
            if not products.exists():
                message = "Ничего не найдено, попробуйте поискать в услугах."
        else:
            products = Product.objects.all()
        services = Service.objects.none()
        about = None
        contacts = None
    elif tab == "services":
        if query:
            services = Service.objects.filter(name__icontains=query)
            if not services.exists():
                message = "Ничего не найдено, попробуйте поискать в продуктах."
        else:
            services = Service.objects.all()
        products = Product.objects.none()
        about = None
        contacts = None
    elif tab == "about":
        about = About.objects.all()
        products = Product.objects.none()
        services = Service.objects.none()
        contacts = Contacts.objects.none()
    elif tab == "contacts":
        contacts = Contacts.objects.all()
        about = About.objects.all()
        products = Product.objects.none()
        services = Service.objects.none()
    else:
        products = Product.objects.all()
        services = Service.objects.all()
        about = None

    context = {
        "products": products,
        "services": services,
        "about": about,
        "tab": tab,
        "contacts": contacts,
        "message": message,
    }

    return render(request, "main/index/index.html", context)
