"""
BS from sketch-a-day
"""
from atproto import Client, models
from villares.token_helpers import get_token

username = get_token('bluesky','USERNAME')
password = get_token('bluesky','APP_PASSWORD')
# Instantiate the client object
client = Client()
client.login(username, password)

# Create and send a new post
#post = client.send_post('Hello World! I posted this via the Python SDK!')

def post(text, image_path=None, alt_text='') -> None:
    if image_path:
        with open(image_path, 'rb') as f:
            img_data = f.read()
        # Add image aspect ratio to prevent default 1:1 aspect ratio
        # Replace with your desired aspect ratio
        aspect_ratio = models.AppBskyEmbedDefs.AspectRatio(height=100, width=100)
        client.send_image(
            text=text,
            image=img_data,
            image_alt=alt_text,
            image_aspect_ratio=aspect_ratio,
        )

# # GIF becomes static
# gif = '/home/villares/GitHub/sketch-a-day/2025/sketch_2025_01_01/sketch_2025_01_01.gif'
# post(
#     "Maybe I'll try to automate posting my daily sketches (https://abav.lugaralgum.com/sketch-a-day) here...",
#     gif, 'animation from my first 2025 sketch showing the numbers 2025 made with colorful lines')     

# # TODO: Check video
# # https://github.com/MarshalX/atproto/blob/main/examples/send_video.py