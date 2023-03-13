import base64
from io import BytesIO
from PIL import Image

# The base64 encoded image data
encoded_image_data = input()

# Remove the header and decode the base64 data
image_data = base64.b64decode(encoded_image_data)

# Load the image data into a PIL Image object
image = Image.open(BytesIO(image_data))

# Show the image
image.show()