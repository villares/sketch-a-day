"""
Toot from sketch-a-day
"""

from time import sleep
from pathlib import Path

from mastodon import Mastodon  # Mastodon.py (pip install mastodon-py)

from villares.token_helpers import get_token

SLEEP = 2 # seconds to wait after submiting image

def mime_type(file):
    if file is None:
        return None
    ff = Path(file).suffix.lstrip('.').lower()
    if ff == 'jpg':
        return 'image/jpeg'
    return f'image/{ff}'

def toot( 
    post_text,
    image_file=None,
    description=None,
    visibility="public",
    language='pt'
):

    access_token = get_token('pynews', 'access_token')
    masto_instance = 'pynews.com.br'
    mastodon = Mastodon(access_token=access_token, api_base_url=masto_instance)
    
    if image_file:
        media = mastodon.media_post(
            image_file, mime_type=mime_type(image_file),
            description=description, focus=None,
            #file_name=None, thumbnail=None,
            #thumbnail_mime_type=None, synchronous=False
            )
        sleep(SLEEP)
        media_ids = [media["id"]]
    else:
        media_ids=[]
    status = mastodon.status_post(
        post_text,
        in_reply_to_id=None,
        media_ids=media_ids,
        language=language,
        visibility=visibility
    )
    print(status)
    return status
