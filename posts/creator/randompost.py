from PIL import Image, ImageDraw, ImageFont, ImageEnhance
from time import sleep
import textwrap
import os
import datetime
import random

from django.conf import settings
mediaroot = settings.MEDIA_ROOT

if os.path.isdir(os.path.join(mediaroot, 'images/')) == False:
    os.mkdir(os.path.join(mediaroot, 'images/'))

if os.path.isdir(os.path.join(mediaroot, 'images/uploads')) == False:
    os.mkdir(os.path.join(mediaroot, 'images/uploads'))

class Posts:

    def createPost(self, text,
        secondary_text='Mentalidade de Homem',
        primary_font_type='BebasNeue Bold.otf',
        primary_font_size=1,
        color = 'white',
        color2 = 'white',
        secondary_font_type='BebasNeue Bold.otf',
        secondary_font_size=1,
        line_sep=1,
        logo_color=False,
        logo_path='',
        logo_size=1,
        dim_factor=0.5,
        greyscale=True,
        preview=False,
        username=''):

        try:
            if os.path.isdir(os.path.join(mediaroot, 'images/created')) == False:
                os.mkdir(os.path.join(mediaroot, 'images/created'))

            # This is to handle the FileResponse function in views
            if os.path.isdir(os.path.join(mediaroot, 'images/download')) == False:
                os.mkdir(os.path.join(mediaroot, 'images/download'))

            if os.path.isdir(os.path.join(mediaroot, 'images/preview')) == False:
                os.mkdir(os.path.join(mediaroot, 'images/preview'))

            if os.path.isdir(os.path.join(mediaroot, 'images/temp/preview')) == False:
                os.mkdir(os.path.join(mediaroot, 'images/temp/preview'))

            IMAGE_DIR = os.path.join(mediaroot, 'images/uploads')
            FONT_DIR = os.path.join(mediaroot, 'fonts')

            text = text.encode('utf-8').decode('ascii', 'ignore')

            if preview:
                IMAGE_DIR = os.path.join(mediaroot, 'images')
                image = Image.open(f'{IMAGE_DIR}/preview.jpg')
            else:
                images = os.listdir(IMAGE_DIR)
                image = random.choice(images)
                image = Image.open(f'{IMAGE_DIR}/{image}')

            RES_B0OST = 2
            w, h = image.size
            new_w = int(w * RES_B0OST)
            new_h = int(h * RES_B0OST)
            image = image.resize((new_w, new_h))

            w, h = image.size #instead check if its square
            if w != h:
                if w < h:
                    box = (0, 0, w, w)
                else:
                    box = (0, 0, h, h)
                image = image.crop(box)

            enhancer = ImageEnhance.Brightness(image)
            image_dimmed = enhancer.enhance(dim_factor)
            image = image_dimmed

            if greyscale == True:
                image = image.convert(mode='L')

            W, H = image.size

            try:
                logo = Image.open(logo_path).convert('RGBA')
                if logo_color:
                    pixels = logo.load()
                    w, h = logo.size
                    for x in range(w):
                        for y in range(h):
                            r, g, b, a = pixels[x, y]
                            # print(r, g, b, a)
                            if (r, g, b) != (255, 255, 255):
                                pixels[x, y] = logo_color #(224, 224, 244, int(255 / 1.2))

                logo = logo.resize(  (int(W/22.5 * logo_size), int(W/22.5 * logo_size))   )
                w, h = logo.size
                image.paste(logo, (int(W/2 - w/2),int(W/2 - w)), logo)
            except:
                print('Provide the logo path')

            draw = ImageDraw.Draw(image)
            font = ImageFont.truetype(os.path.join(FONT_DIR, f'{primary_font_type}'), size=int((W / 12.5 * primary_font_size)))
            if len(text) > 110:
                font = ImageFont.truetype(os.path.join(FONT_DIR, f'{primary_font_type}'), size=int((W / 16 * primary_font_size)))

            lines = textwrap.wrap(text, width=20)
            y_text = H

            for line in lines:
                width, height = font.getsize(line)
                draw.text(((W - width) / 2, y_text / 2), line, fill=color, font=font)
                y_text += height * 2.2 * line_sep


            font = ImageFont.truetype(os.path.join(FONT_DIR, f'{secondary_font_type}'), size=int((W / 50 * secondary_font_size)))
            text = secondary_text
            lines = textwrap.wrap(text, width=40)
            for line in lines:
                width, height = font.getsize(line)
                draw.text(((W - width) / 2, y_text / 2), line, fill=color2, font=font)
                y_text += height * 2.2

            if preview == True:
                w, h = image.size
                image = image.resize(  ( int(w/4), int(h/4)   )   )

                time = str(datetime.datetime.now()).replace(':', '.')
                image.save(os.path.join(mediaroot, f"images/preview/preview_{username}.png"))
                image.save(os.path.join(mediaroot, f"images/temp/preview/preview_{username}_{time}.png"))
                return f"preview_{username}_{time}.png"
            else:
                time = str(datetime.datetime.now()).replace(':', '.')
                image.save(os.path.join(mediaroot, f"images/download/image{time}.png"))

                # font = ImageFont.truetype(f'fonts/{secondary_font_type}', size=int((W / 40 * secondary_font_size)))
                # text = 'Please, click heart icon to get no watermark image.'
                # lines = textwrap.wrap(text, width=40)
                # for line in lines:
                #     width, height = font.getsize(line)
                #     draw.text(((W - width) / 2, y_text / 1.9), line, fill='rgba(255, 255, 255, 0)', font=font)
                #     y_text += height * 2.2

                w, h = image.size
                image = image.resize(  ( int(w/5), int(h/5)   )   )

                image.save(os.path.join(mediaroot, f"images/created/image{time}.png"))
                return f"image{time}.png"

        except IndexError:
            print('Please upload an image to current directory /images/uploads')
