from django.shortcuts import render, get_object_or_404
import requests
import base64
from PIL import Image as PILImage
import io
from app.models import Product, Image

# Hugging Face API details
API_URL = "https://api-inference.huggingface.co/models/ZB-Tech/Text-to-Image"
headers = {"Authorization": "Bearer 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"}

# Function to query the Hugging Face API
def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code != 200:
        raise Exception(f"Error: {response.status_code}, {response.text}")
    return response.content

def generate_image(request):
    image_data = None
    error_message = None
    gallery = Product.objects.all()  # Get all products for the gallery

    if request.method == 'POST':
        prompt = request.POST.get('prompt')
        style = request.POST.get('style')  # Get the selected style from the form

        if prompt and style:
            try:
                # Send the prompt to the API
                image_bytes = query({"inputs": prompt})  # Adjust according to API requirements

                # Open the image
                image = PILImage.open(io.BytesIO(image_bytes))

                # Convert the image to a format that can be rendered in the template
                img_io = io.BytesIO()
                image.save(img_io, 'PNG')
                img_io.seek(0)
                image_data = base64.b64encode(img_io.read()).decode('utf-8')

                # Render the result template with the image and gallery
                return render(request, 'result.html', {
                    'prompt': prompt,
                    'style': style,
                    'image_data': image_data,
                    'gallery': gallery,  # Pass the gallery to the template
                })
            except Exception as e:
                error_message = str(e)

    # Render the form if GET request or no valid input
    return render(request, 'jamal.html', {'error': error_message, 'gallery': gallery})




