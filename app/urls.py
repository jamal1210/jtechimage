from django.urls import path,include
from app import views as app_views
from aiimage import views as aiimage_views




urlpatterns = [
    # main 
    path('', aiimage_views.generate_image, name='index.html'),
    
    #ai image sections
    path('ho/', app_views.home_page, name='home.html'),  # Home page for general images
    path('image/<int:id>/<slug:slug>/', app_views.details_view, name='details'),  # General image details
    path('search/', app_views.search_page, name='search.html'),  # General image search
    
    # Sports section
    path('sports/', app_views.sports_gallery, name='sports.html'),  # Sports gallery page
    path('sports/<int:id>/<slug:slug>/', app_views.sports_details_view, name='detailss'),  # Sports image details
    path('sports_search/', app_views.sports_search_page, name='search1'),  # Sports image search

    # image slider sections
    path('slider/', app_views.slider, name='sliders'),

    #vector store 
    path('vector/', app_views.vector_store, name='vector.html'),  # Home page for general images
    path('vector_view/<int:id>/<slug:slug>/', app_views.vector_view, name='vectors'),  # General image details
    path('vector_search/', app_views.vector_search_page, name='vector_search.html'),  # General image search

    # contract page and about page 
    path('contact/', app_views.contact_view, name='contact.html'),
    path('about/', app_views.about_page, name='about.html')

]
