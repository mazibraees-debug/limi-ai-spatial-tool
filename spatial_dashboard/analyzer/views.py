from django.shortcuts import render
from django.conf import settings
import os
import threading
from .ml_models.lighting_generator import generate_lighting
from .ml_models.vision_detection import analyze_room

def generate_thread(uploaded_image_path, output_path, lighting):
    generate_lighting(uploaded_image_path, output_path, lighting)

def home(request):
    processed_image_url = None
    uploaded_image_url = None
    analysis = None

    if request.method == "POST" and request.FILES.get("image"):
        image_file = request.FILES["image"]

        os.makedirs(settings.MEDIA_ROOT, exist_ok=True)
        # save uploaded file
        uploaded_image_path = os.path.join(settings.MEDIA_ROOT, image_file.name)
        with open(uploaded_image_path, 'wb+') as f:
            for chunk in image_file.chunks():
                f.write(chunk)

        uploaded_image_url = settings.MEDIA_URL + image_file.name

        # analyze room
        analysis = analyze_room(uploaded_image_path)

        # generate AI lighting image in background
        output_filename = f"processed_{image_file.name}"
        output_path = os.path.join(settings.MEDIA_ROOT, output_filename)
        processed_image_url = settings.MEDIA_URL + output_filename
        threading.Thread(target=generate_thread, args=(uploaded_image_path, output_path, analysis['lighting'])).start()

    return render(request, "index.html", {
        "uploaded_image": uploaded_image_url,
        "processed_image": processed_image_url,
        "analysis": analysis
    })