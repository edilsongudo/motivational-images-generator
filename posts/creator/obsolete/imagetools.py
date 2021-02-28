from PIL import Image, ImageEnhance
import os
from django.conf import settings


def imagetooldim(self, factor=0.5, filename=''):
    mediaroot = settings.MEDIA_ROOT
    image = Image.open(os.path.join(mediaroot, f'images/created/{filename}'))
    enhancer = ImageEnhance.Brightness(image)
    image = enhancer.enhance(factor)
    image.save(os.path.join(mediaroot, f'images/created/{filename}'))
    print(f'{filename} dimmed')
