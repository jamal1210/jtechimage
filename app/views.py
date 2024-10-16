from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Image, Sports_Image_page
from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Contact_page,image_slider,vector_page
from django.contrib import messages


# Home page for general images

def home_page(request):
    images = Image.objects.all()  # Renamed 'frm' to 'images' for clarity
    return render(request, 'home.html', {'images': images})


# Detail view for general images
def details_view(request, id, slug):
    image = get_object_or_404(Image, id=id, slug=slug)  # Renamed 'frm' to 'image' for clarity
    return render(request, 'detail.html', {'image': image})


# General search page
def search_page(request):
    query = request.GET.get('search', None)  # Get the search query from the GET parameters
    result = []  # Initialize an empty result list

    if query:  # Proceed only if there is a query
        result = Image.objects.filter(Q(title__icontains=query) | Q(tags__icontains=query))

    return render(request, 'search.html', {'query': query, 'result': result})



# Sports gallery page

def sports_gallery(request):  # Fixed 'galary' to 'gallery'
    sports_images = Sports_Image_page.objects.all()  # Use 'sports_images' to make it clearer
    return render(request, 'sports.html', {'sports_images': sports_images})


# Detail view for sports images
def sports_details_view(request, id, slug):
    sports_image = get_object_or_404(Sports_Image_page, id=id, slug=slug)
    return render(request, 'details1.html', {'Sports_Image_page': sports_image})


# Search for sports images
def sports_search_page(request):
    query = request.GET.get('searchs1', None)
    result = []  # Initialize an empty result list

    if query:
        result = Sports_Image_page.objects.filter(Q(title__icontains=query) | Q(tags__icontains=query))

    return render(request, 'searchs1.html', {'query': query, 'result': result})


# contact page 

def contact_view(request):
    if request.method == 'POST':
        # Process form data here (saving to the database, sending an email, etc.)
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # After processing the form data, redirect to the "home" page
        return redirect('index.html')  # 'home' should be the name of your URL pattern for the home page

    # Render the contact form if it's a GET request
    return render(request, 'contact.html')


    #slider image 

def slider(request):
    gallery = image_slider.objects.all()  # Use the correct model name 'Image'
    return render(request, 'index.html', {'gallery': gallery})


#vector store 

def vector_store(request):  # Fixed 'galary' to 'gallery'
    vector_store = vector_page.objects.all()  # Use 'sports_images' to make it clearer
    return render(request, 'vector.html', {'vector_store': vector_store})


# Detail view for sports images

def vector_view(request, id, slug):
    vector_store = get_object_or_404(vector_page, id=id, slug=slug)
    return render(request, 'vector_view.html', {'vector_store': vector_store})


# Search for sports images
def vector_search_page(request):
    query = request.GET.get('searchs1', None)
    result = []  # Initialize an empty result list

    if query:
        result = vector_page.objects.filter(Q(title__icontains=query) | Q(tags__icontains=query))

    return render(request, 'vector_view.html', {'query': query, 'result': result})



# about page 

def about_page(request):
    return render(request,'about.html')