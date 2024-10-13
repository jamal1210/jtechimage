from django.urls import path,include
from app import views as app_views
from aiimage import views as aiimage_views

urlpatterns = [
    path('', aiimage_views.generate_image, name='jamal.html'),
    
    #ai image sections
    path('ho/', app_views.home_page, name='home.html'),  # Home page for general images
    
    path('image/<int:id>/<slug:slug>/', app_views.details_view, name='details'),  # General image details
    path('search/', app_views.search_page, name='search.html'),  # General image search
    
    # Sports section
    path('sports/', app_views.sports_gallery, name='sports.html'),  # Sports gallery page
    path('sports/<int:id>/<slug:slug>/', app_views.sports_details_view, name='detailss'),  # Sports image details
    path('sports_search/', app_views.sports_search_page, name='search1'),  # Sports image search
    path('contact/', app_views.contact_view, name='contact.html'),

]
