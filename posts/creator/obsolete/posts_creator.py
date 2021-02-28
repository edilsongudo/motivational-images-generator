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

if os.path.isdir(os.path.join(mediaroot, 'images/zapya')) == False:
    os.mkdir(os.path.join(mediaroot, 'images/zapya'))

class Posts:

    def resize(self):

        if os.path.isdir(os.path.join(mediaroot, 'images/resized')) == False:
            os.mkdir(os.path.join(mediaroot, 'images/resized'))

        images = os.listdir(os.path.join(mediaroot, 'images/zapya'))

        n = 1
        for image in images:
            filename = image
            resized = os.listdir(os.path.join(mediaroot, 'images/resized'))

            if filename not in resized:

                try:
                    image = Image.open(os.path.join(mediaroot, f'images/zapya/{image}'))

                    w, h = image.size

                    if w < h:
                        box = (0, 0, w, w)
                    else:
                        box = (0, 0, h, h)

                    image2 = image.crop(box)
                    image2.save(os.path.join(mediaroot, f'images/resized/{filename}'))
                    print(f'Image {n} croped')
                except Exception as e:
                    print(e)
                n += 1

            else:
                print('Image already resized')

    def dim(self):

        if os.path.isdir(os.path.join(mediaroot, 'images/dimmed')) == False:
            os.mkdir(os.path.join(mediaroot, 'images/dimmed'))

        factor = 0.5

        images = os.listdir(os.path.join(mediaroot, 'images/resized'))

        n = 1
        for image in images:
            filename = image
            dimmed = os.listdir(os.path.join(mediaroot, 'images/dimmed'))

            if filename not in dimmed:
                try:
                    image = Image.open(os.path.join(mediaroot, f'images/resized/{image}'))

                    enhancer = ImageEnhance.Brightness(image)
                    image = enhancer.enhance(factor)

                    image.save(os.path.join(mediaroot, f'images/dimmed/{filename}'))
                    print(f'Image {n} dimmed')
                except Exception as e:
                    print(e)
                n += 1
            else:
                print('Image already dimmed.')


    def greyscale(self):
        if os.path.isdir(os.path.join(mediaroot, 'images/ready')) == False:
            os.mkdir(os.path.join(mediaroot, 'images/ready'))

        images = os.listdir(os.path.join(mediaroot, 'images/dimmed'))

        n = 1
        for image in images:
            filename = image
            ready = os.listdir(os.path.join(mediaroot, 'images/ready'))

            if filename not in ready:
                try:
                    image2 = Image.open(os.path.join(mediaroot, f'images/dimmed/{image}'))

                    image2 = image2.convert(mode='L')

                    image2.save(os.path.join(mediaroot, f'images/ready/{filename}'))
                    print(f'Image {n} turned greyish')
                except Exception as e:
                    print(e)
                n += 1
            else:
                print('Image already turned greyish.')

    def createPost(self, text,
        secondary_text='Mentalidade de Homem',
        primary_font_type='BebasNeue Bold.otf',
        primary_font_size=1,
        color = 'white',
        secondary_font_type='BebasNeue Bold.otf',
        secondary_font_size=1,
        line_sep=1,
        logo=False,
        logo_color=False,
        logo_path='',
        logo_size=1,
        resize=True,
        dim=True,
        greyscale=True,
        debug=False):

        if debug:
            print('Debug is OFF, images will not resized, dimmed or turned grey.')

        try:
            if os.path.isdir(os.path.join(mediaroot, 'images/created')) == False:
                os.mkdir(os.path.join(mediaroot, 'images/created'))

            if greyscale == True:
                if debug:
                    self.resize()
                    self.dim()
                    self.greyscale()
                images = os.listdir(os.path.join(mediaroot, 'images/ready'))
                IMAGE_DIR = os.path.join(mediaroot, 'images/ready')
            else:
                if dim == True:
                    if debug:
                        self.resize()
                        self.dim()
                    images = os.listdir(os.path.join(mediaroot, 'images/dimmed'))
                    IMAGE_DIR = os.path.join(mediaroot, 'images/dimmed')
                else:
                    if debug:
                        self.resize()
                    images = os.listdir(os.path.join(mediaroot, 'images/resized'))
                    IMAGE_DIR = os.path.join(mediaroot, 'images/resized')

            n = 1
            for text in text:
                text = text.encode('utf-8').decode('ascii', 'ignore')

                image = random.choice(images)
                image = Image.open(f'{IMAGE_DIR}/{image}')
                W, H = image.size

                if logo:
                    try:
                        logo = Image.open(logo_path).convert('RGBA')
                    except:
                        print('Provide the logo path')
                        break

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

                draw = ImageDraw.Draw(image)

                font = ImageFont.truetype(primary_font_type, size=int((W / 12.5 * primary_font_size)))
                if len(text) > 110:
                    font = ImageFont.truetype(primary_font_type, size=int((W / 16 * primary_font_size)))

                lines = textwrap.wrap(text, width=20)
                y_text = H

                for line in lines:
                    width, height = font.getsize(line)
                    draw.text(((W - width) / 2, y_text / 2), line, fill=color, font=font)
                    y_text += height * 2.2 * line_sep

                font = ImageFont.truetype(secondary_font_type, size=int((W / 50 * secondary_font_size)))
                text = secondary_text
                lines = textwrap.wrap(text, width=40)
                for line in lines:
                    width, height = font.getsize(line)
                    draw.text(((W - width) / 2, y_text / 2), line, fill=color, font=font)
                    y_text += height * 2.2
                image.save(os.path.join(mediaroot, f"images/created/image{str(datetime.datetime.now()).replace(':', '.')}.png"))
                print(f'Post {n} created.')
                n += 1
        except IndexError:
            print('Please upload an image to current directory /images/zapya')
