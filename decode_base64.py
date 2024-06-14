import base64
from PIL import Image
import io

base64_image = (
    "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/wcAAwAB/4kbQgAAAAAASUVORK5CYII="
)

try:
    image_data = base64.b64decode(base64_image)
    image = Image.open(io.BytesIO(image_data))
    image.show()  # This should display the image if it's valid
    print("Image is valid and displayed successfully.")
except Exception as e:
    print(f"Error: {e}")
