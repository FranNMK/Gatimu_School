from django.shortcuts import render

# Create your views here.

def home(request):
    info = SchoolInfo.objects.first()
    return render(request, 'website/home.html', {'info': info})

from .models import SchoolInfo

def about(request):
    info = SchoolInfo.objects.first()
    return render(request, 'website/about.html', {'info': info})

from .models import GalleryImage

def gallery(request):
    images = GalleryImage.objects.all().order_by('-created_at')
    return render(request, 'website/gallery.html', {'images': images})


from .forms import ContactForm
from django.contrib import messages
from django.shortcuts import render, redirect

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')
    else:
        form = ContactForm()
    
    return render(request, 'website/contact.html', {'form': form})

def portal(request):
    return render(request, 'website/portal.html')
