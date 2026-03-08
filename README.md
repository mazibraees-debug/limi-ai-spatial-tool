---
title: Limi AI Spatial Analysis Tool
emoji: 🏠
colorFrom: blue
colorTo: gray
sdk: docker
app_file: spatial_dashboard/manage.py
pinned: false
---

# Limi AI Spatial Analysis & Interior Refinement Tool

## Overview

This project is a **Spatial Analysis & Interior Refinement Tool** built for Limi AI, focusing on "Ambient Infrastructure." It combines computer vision for real-time room analysis with generative AI for lighting refinement, presented through a modern, dark-mode UI. The tool analyzes uploaded room images to detect lighting type, room type, and occupancy, then generates AI-refined versions with improved lighting based on the analysis.

This implementation fulfills the technical assessment requirements, integrating OpenCV-based vision detection, Diffusers for generative refinement, and a Django-based dashboard with a clean, neon-accented UI.

## Features

### 1. Computer Vision & Attribute Detection
- **Detection Capabilities**:
  - **Lighting Type**: Natural, Artificial, or Artificial Dim (based on image brightness).
  - **Room Type**: Bedroom, Office, or Living Room (inferred from detected objects using YOLOv8).
  - **Presence Detection**: Checks for human presence in the room.
- **Output**: Real-time JSON logging of spatial attributes (printed to console).
- **Tech**: Uses OpenCV for image processing and Ultralytics YOLOv8 for object detection.

### 2. Generative Refinement (Stable Diffusion)
- **Workflow**: Image-to-Image generation using Hugging Face Diffusers.
- **Logic**: Re-imagines room lighting conditionally:
  - If "Artificial Dim" is detected → Applies "Cyberpunk Ambient Lighting."
  - If "Artificial" → Applies "Artificial Lighting."
  - If "Natural" → Applies "Warm Sunlight."
- **Optimization**: Runs on CPU with `low_cpu_mem_usage=True`, `torch.float16`, and image resizing for efficiency.
- **Tech**: Stable Diffusion v1-5 pipeline via Diffusers.

### 3. Limi AI Dashboard (UI)
- **Framework**: Django backend with HTML/CSS/JS frontend.
- **UI Layout**:
  - **Upload Zone**: File input for room photos.
  - **Live Analysis Panel**: Displays "Spatial Stats" with dynamic badges (e.g., Detected Room, Lighting, Occupancy).
  - **Visual Comparison**: Side-by-side view of Original vs. AI-Refined images.
- **Styling**: Custom CSS with dark mode and neon accents (green/blue) for a "Clean Tech" aesthetic.
- **Interactivity**: Analysis results show immediately; image generation runs asynchronously with a loading spinner that updates via JavaScript polling.

## Tech Stack
- **Backend**: Django 6.0.3
- **ML/AI**:
  - Computer Vision: OpenCV, Ultralytics YOLOv8
  - Generative AI: Hugging Face Diffusers, Stable Diffusion
- **Frontend**: HTML, CSS, JavaScript
- **Dependencies**: See `requirements.txt` (includes Torch, PIL, etc.)
- **Other**: Python 3.x, Git for version control

## Installation

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd limi-ai-spatial-tool
   ```

2. **Set Up Virtual Environment**:
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Download Model Weights**:
   - The YOLOv8n model (`yolov8n.pt`) is included in the project. If missing, it will download automatically on first run.

5. **Run Migrations** (if needed for Django):
   ```bash
   cd spatial_dashboard
   python manage.py migrate
   ```

## Usage

1. **Start the Server**:
   ```bash
   python manage.py runserver
   ```
   - Access the dashboard at `http://127.0.0.1:8000/`.

2. **Upload an Image**:
   - Use the upload form to select a room photo (JPG/PNG).
   - The tool will:
     - Analyze the image for spatial attributes (results appear instantly in the "Spatial Stats" panel).
     - Generate an AI-refined version in the background (loading indicator shows progress; updates automatically when ready).

3. **View Results**:
   - **Stats Panel**: See detected room type, lighting, and occupancy.
   - **Images**: Compare Original vs. AI-Refined side-by-side.

## Project Structure
```
limi-ai-spatial-tool/
├── .gitignore                 # Ignores venv, media, logs, etc.
├── requirements.txt           # Python dependencies
├── Dockerfile                 # For containerized deployment
├── spatial_dashboard/         # Django project root
│   ├── manage.py
│   ├── spatial_dashboard/     # Project settings
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── ...
│   ├── analyzer/              # Main app
│   │   ├── models.py
│   │   ├── views.py           # Handles upload, analysis, generation
│   │   ├── urls.py
│   │   ├── templates/
│   │   │   └── index.html     # Dashboard UI
│   │   ├── static/
│   │   │   └── style.css      # Dark mode styling
│   │   └── ml_models/         # AI logic
│   │       ├── vision_detection.py  # CV detection
│   │       └── lighting_generator.py # Generative refinement
│   ├── media/                 # Uploaded/generated images (ignored)
│   └── uploads/               # Additional uploads (ignored)
└── venv/                      # Virtual environment (ignored)
```

## How It Works
1. **Image Upload**: User uploads a room image via the Django form.
2. **Vision Analysis**: `vision_detection.py` processes the image:
   - Uses YOLO to detect objects and infer room type.
   - Calculates brightness for lighting type.
   - Checks for persons.
   - Outputs JSON to console.
3. **Generative Refinement**: `lighting_generator.py` runs asynchronously:
   - Uses Stable Diffusion to re-imagine lighting based on detection.
   - Saves refined image to media/.
4. **UI Updates**: Page renders with analysis stats immediately. JavaScript polls for the refined image and displays it when ready.

## Deployment on Hugging Face Spaces

This project is containerized with Docker for easy deployment on Hugging Face Spaces.

1. **Push to GitHub**: Upload the code to a public GitHub repository.
2. **Create a Space**: Go to [Hugging Face Spaces](https://huggingface.co/spaces), create a new Space, select "Docker" as the SDK, and link your repo.
3. **Configuration**: The Space will use the provided `Dockerfile` to build and run the app. It exposes port 8000.
4. **Access**: Once deployed, the app will be available at `https://your-username-space-name.hf.space`.

Note: Due to resource constraints on free Spaces (CPU-only, limited RAM), image generation may be slow. Consider upgrading to a paid tier for better performance.

## Evaluation Notes
- **Model Integration**: Seamless backend triggering with async generation and loading states.
- **UI/UX Design**: Professional dark-mode interface with neon accents; responsive and clean.
- **Inference Speed**: Optimized for CPU (float16, low memory); generation takes 1-5 minutes but doesn't block analysis.
- **Code Structure**: ML logic separated into `ml_models/`; views handle UI integration cleanly.

## Contributing
- Fork the repo and submit pull requests.
- Ensure code follows PEP8 and includes tests for ML components.

## License
This project is proprietary to Limi AI. Contact for usage permissions.

## Candidate
Muhammad Azib - AI/ML Engineer Assessment Submission