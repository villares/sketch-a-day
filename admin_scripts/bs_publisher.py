"""
BS from sketch-a-day
"""
import re
import subprocess
import tempfile
from pathlib import Path

from atproto import Client, models
from villares.token_helpers import get_token

username = get_token('bluesky','USERNAME')
password = get_token('bluesky','APP_PASSWORD')


def mime_type(file):
    if file is None:
        return None
    ff = Path(file).suffix.lstrip('.').lower()
    if ff == 'jpg':
        return 'image/jpeg'
    return f'image/{ff}'
 
def _gif_to_mp4(gif_path):
    """Convert a GIF file to an MP4 using ffmpeg, returning the temp Path."""
    tmp = Path(tempfile.mktemp(suffix='.mp4'))
    subprocess.run(
        [
            'ffmpeg',
            '-i', str(gif_path),
            '-movflags', 'faststart',
            '-pix_fmt', 'yuv420p',
            # Ensure dimensions are divisible by 2 (required by most H.264 encoders)
            '-vf', 'scale=trunc(iw/2)*2:trunc(ih/2)*2',
            '-y', str(tmp),
        ],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    return tmp

def _parse_facets(text):
    """
    Detect URLs in text and return a list of BlueSky rich-text facets so that
    links are clickable in posts. Byte offsets are used, as required by the AT
    Protocol.
    """
    facets = []
    url_pattern = re.compile(r'https?://[^\s\]>\"\']+')
    for match in url_pattern.finditer(text):
        url = match.group().rstrip('.,;:!?)')  # strip trailing punctuation
        byte_start = len(text[:match.start()].encode('utf-8'))
        byte_end = byte_start + len(url.encode('utf-8'))
        facets.append(
            models.AppBskyRichtextFacet.Main(
                features=[models.AppBskyRichtextFacet.Link(uri=url)],
                index=models.AppBskyRichtextFacet.ByteSlice(
                    byte_start=byte_start,
                    byte_end=byte_end,
                ),
            )
        )
    return facets or None

def post(
    post_text,
    image_file=None,
    description=None,
    language=None,    #  language tag ('en', 'pt', etc.).
):
    """
    Post to BlueSky.
    """
    # Instantiate the client object
    client = Client()
    client.login(username, password)
    if len(post_text) > 299:
        print('Truncating post. Bluesky post limit is 300 graphemes.')
        post_text = post_text[:298] + '…' 
    facets = _parse_facets(post_text)
    langs = [language] if language else None
    tmp_video = None
    try:
        if image_file:
            image_file = Path(image_file)
            if image_file.suffix.lower() == '.gif':
                # BlueSky does not animate GIFs — convert to video first
                tmp_video = _gif_to_mp4(image_file)
                status = client.send_video(
                    text=post_text,
                    video=tmp_video.read_bytes(),
                    video_alt=description or '',
                    facets=facets,
                    langs=langs,
                )
            else:
                status = client.send_image(
                    text=post_text,
                    image=image_file.read_bytes(),
                    image_alt=description or '',
                    facets=facets,
                    langs=langs,
                )
        else:
            status = client.send_post(
                text=post_text,
                facets=facets,
                langs=langs,
            )
    finally:
        if tmp_video and tmp_video.exists():
            tmp_video.unlink()
    print(status)
    return status

# Test post
p = """#GIF #animation #loop\nFind the sketch-a-day archives and tip jar at: https://abav.lugaralgum.com/sketch-a-day
Code for this sketch at: https://github.com/villares/sketch-a-day/tree/main/2026/sketch_2026_02_12 #Processing #Python #py5 #CreativeCoding"""
g = Path('/home/villares/GitHub/sketch-a-day/2026/sketch_2026_02_12/sketch_2026_02_12.gif')
d = 'Animation of two circles that grow and shrink changing colors'
