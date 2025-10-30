from django.shortcuts import render,redirect
from .models import Cars
from django.shortcuts import get_object_or_404
from django.contrib import messages
from .forms import ContactForm
from django.http import HttpResponse
from django.contrib.auth.models import User


# Create your views here.
def AllCars(request):
    mycars = Cars.objects.all()
    return render(request, 'myapp/cars.html', {'mycars': mycars})

def Car_des(request, car_id):
    car = get_object_or_404(Cars, pk=car_id)
    return render(request, 'myapp/car_description.html', {'car': car})

def About(request):
    return render(request, 'myapp/about.html')


def Contact(request):
    # if request.method == "POST":
    #     form = ContactForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         messages.success(request, "Thank you for contacting us! We'll get back to you soon.")
    #         return redirect('contact')
    # else:
    #     form = ContactForm()

    # return render(request, 'myapp/contact.html', {'form': form})
    form_submitted = False  # Track karega ke form submit hua ya nahi

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            form_submitted = True  # True ho gaya matlab form submit hua
    else:
        form = ContactForm()

    return render(request, 'myapp/contact.html', {
        'form': form,
        'form_submitted': form_submitted
    })
def create_admin(request):
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser("admin", "admin@example.com", "adminpassword")
        return HttpResponse("✅ Superuser created successfully!")
    else:
        return HttpResponse("⚠️ Superuser already exists!")