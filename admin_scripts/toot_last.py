"""
Toot from sketch-a-day
"""

from pathlib import Path

import tomli as tomllib # tomllib will be in Python 3.11's standard library only
from mastodon import Mastodon

with open("/home/villares/api_tokens", "rb") as f:
    api_tokens = tomllib.load(f)
    
access_token = api_tokens['pynews']['access_token']

m = Mastodon(access_token=access_token)

metadata = m.media_post("image.png", "image/png")
# Response format: https://mastodonpy.readthedocs.io/en/stable/#media-dicts
m.status_post("This post contains previously uploaded image.png", media_ids=metadata["id"])