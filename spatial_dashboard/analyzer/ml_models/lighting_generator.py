import torch
from diffusers import StableDiffusionImg2ImgPipeline
from PIL import Image

# Select device (CPU only, since no GPU)
device = "cpu"

# Load the model safely on CPU with reduced memory usage
pipe = StableDiffusionImg2ImgPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch.float16,
    low_cpu_mem_usage=True
)
pipe.to(device)

# Maximum image size to reduce memory consumption
MAX_SIZE = (512, 512)

def generate_lighting(image_path, output_path, lighting):
    # Open image and convert to RGB
    image = Image.open(image_path).convert("RGB")
    
    # Resize image to MAX_SIZE if needed
    image.thumbnail(MAX_SIZE)

    # Prompt for the lighting effect based on detected lighting
    if lighting == "Artificial Dim":
        prompt = "beautiful cyberpunk ambient lighting in modern room"
    elif lighting == "Artificial":
        prompt = "beautiful artificial lighting in modern room"
    else:  # Natural
        prompt = "beautiful natural warm sunlight in modern room"

    # Inference without storing gradients to save RAM
    with torch.no_grad():
        result = pipe(
            prompt=prompt,
            image=image,
            strength=0.6,
            guidance_scale=7.5
        ).images[0]

    # Save the result
    result.save(output_path)

    return output_path