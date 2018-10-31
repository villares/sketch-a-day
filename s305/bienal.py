import json
from collections import namedtuple

try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen


def http_get(url):
    response = urlopen(url)
    return response.read()


def get_deep_ai_caption_position(img_width, img_height, caption):
    """
    Deep AI scales image limiting a max of 800 for height or width
    Here we're reversing this scale so we can draw the boxes in the image
    """
    scale = 1 / (float(800) / max(img_width, img_height))
    box = caption['bounding_box']
    top = int(box[0] * scale)
    left = int(box[1] * scale)
    right = int(left + box[3] * scale)
    bottom = int(top + box[2] * scale)
    return (top, left), (bottom, right)


AWS = namedtuple('AWS', ['faces', 'celebs', 'labels'])
IBM = namedtuple('IBM', ['faces', 'main'])
GOOGLE = namedtuple('Google', [
    'web_detection',
    'text_annotations',
    'full_text_annotation',
    'label_annotation',
    'crop_hint_annotation',
    'safe_search_annotation',
    'image_properties_annotation',
])
AZURE = namedtuple('Azure', [
    "faces",
    "tags",
    "adult",
    "color",
    "categories",
    "description",
])
DEEP_AI = namedtuple('DeepAI', ['dense_cap'])
CLARIFAI = namedtuple('Clarifai', [
    "nsfw",
    "general",
    "moderation",
    "celebrities",
    "demographics",
])


class ImageAnalysis():
    """
    Holds an image dict and exposes it via an API
    """

    def __init__(self, data):
        self.data = data

    def __getitem__(self, key):
        return self.data[key]

    @property
    def aws(self):
        data = self.data['amazonRekog']
        return AWS(
            data.get('faces', {}),
            data.get('celebs', {}),
            data.get('labels', {}),
        )

    @property
    def ibm(self):
        data = self.data['ibmwatson']
        return IBM(
            data.get('faces', {}),
            data.get('main', {})
        )

    @property
    def google(self):
        data = self.data['googlecloud']
        return GOOGLE(
            data.get('webDetection', {}),
            data.get('textAnnotations', {}),
            data.get('fullTextAnnotation', {}),
            data.get('labelAnnotations', {}),
            data.get('cropHintsAnnotation', {}),
            data.get('safeSearchAnnotation', {}),
            data.get('imagePropertiesAnnotation', {}),
        )

    @property
    def azure(self):
        data = self.data['microsoftazure']['main']
        return AZURE(
            data.get('faces', {}),
            data.get('tags', {}),
            data.get('adult', {}),
            data.get('color', {}),
            data.get('categories', {}),
            data.get('description', {}),
        )

    @property
    def deep_ai(self):
        return DEEP_AI(self.data['deepAi'].get('DenseCap', {}))

    @property
    def clarifai(self):
        data = self.data['clarifai']
        return CLARIFAI(
            data.get('nsfw', {}),
            data.get('general', {}),
            data.get('moderation', {}),
            data.get('celebrities', {}),
            data.get('demographics', {}),
        )

    def __repr__(self):
        return '<(Image) ID {} >'.format(self.data['pk'])


class Collection():
    """
    Holds an image dict and exposes it via an API
    """

    def __init__(self, data):
        self.data = data

    def __getitem__(self, key):
        return self.data[key]

    @property
    def images(self):
        if 'images' not in self.data:
            api = ArtDecoderApi()
            self.data = api.get_collection(self.data['id'])
        return [ImageAnalysis(i) for i in self.data['images']]

    def __repr__(self):
        return '<(Collection) ID {} >'.format(self.data['id'])


class ArtDecoderApi():
    HOST = 'art-decoder.bienal.berinfontes.com'

    def _url(self, path, secure=True):
        if secure:
            protocol = 'https://'
        else:
            protocol = 'http://'
        return protocol + self.HOST + path

    def get_all_collections(self):
        content = http_get(self._url('/api/collection'))
        return json.loads(content)

    def get_collection(self, col_id):
        path = '/api/collection/{}'.format(col_id)
        content = http_get(self._url(path))
        return json.loads(content)

    def get_collection_image(self, col_id, image_id):
        path = '/api/collection/{}/image/{}'.format(col_id, image_id)
        content = http_get(self._url(path))
        return json.loads(content)


class BienalClient():

    def __init__(self):
        self.api = ArtDecoderApi()

    def get_all_collections(self):
        return [Collection(c) for c in self.api.get_all_collections()]

    def get_collection(self, col_id):
        return Collection(self.api.get_collection(col_id))

    def get_collection_image(self, col_id, image_id):
        return ImageAnalysis(self.api.get_collection_image(col_id, image_id))
