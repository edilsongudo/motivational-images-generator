from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from .utils import generate_ref_code

# Create your models here.

fonts = (
    ('BebasNeue Bold', 'BebasNeue Bold'),
    ('BebasNeue Book', 'BebasNeue Book'),
    ('big_noodle_titling_oblique', 'big_noodle_titling_oblique'),
    ('big_noodle_titling', 'big_noodle_titling'),
    ('BRADHITC', 'BRADHITC'),
    ('CHILLER', 'CHILLER'),
    ('COLONNA', 'COLONNA'),
    ('comic', 'comic'),
    ('comicbd', 'comicbd'),
    ('cordia', 'cordia'),
    ('cordiab', 'cordiab'),
    ('cordiai', 'cordiai'),
    ('cordiau', 'cordiau'),
    ('cordiaub', 'cordiaub'),
    ('cordiaui', 'cordiaui'),
    ('cordiauz', 'cordiauz'),
    ('CURLZ___', 'CURLZ___'),
    ('FORTE', 'FORTE'),
    ('FREESCPT', 'FREESCPT'),
    ('FRSCRIPT', 'FRSCRIPT'),
    ('Gabriola', 'Gabriola'),
    ('HARNGTON', 'HARNGTON'),
    ('JOKERMAN', 'JOKERMAN'),
    ('MISTRAL', 'MISTRAL'),
    ('PRISTINA', 'PRISTINA'),
    ('RAGE', 'RAGE'),
    ('segoepr', 'segoepr'),
    ('segoeprb', 'segoeprb'),
)

languages = (('English', 'English'), ('Portuguese', 'Portuguese'))


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE)
    code = models.CharField(max_length=12, blank=True, default='')
    recommended_by = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True, related_name='ref_by')
    ref_code_clicks = models.IntegerField(default=0)
    connects = models.IntegerField(default=10)
    money = models.FloatField(default=0.0)
    language = models.CharField(
        max_length=30, default='English', choices=languages)
    last_image_downloaded = models.CharField(
        max_length=70, default='', blank=True)
    number_of_posts_created = models.IntegerField(
        default=0)
    number_of_posts_downloaded = models.IntegerField(
        default=0, blank=True)
    primary_text_color = models.CharField(
        max_length=30, default='#ffffff')
    primary_font_type = models.CharField(
        max_length=30, default='BebasNeue Bold', choices=fonts)
    primary_font_size = models.IntegerField(
        default=50, validators=[MinValueValidator(0), MaxValueValidator(100)])
    brand_name = models.CharField(
        max_length=30, default='@yourbrandname')
    brand_name_font_type = models.CharField(
        max_length=50, default='BebasNeue Book', choices=fonts)
    brand_name_font_size = models.IntegerField(
        default=100, validators=[MinValueValidator(0), MaxValueValidator(100)])
    brand_name_font_color = models.CharField(
        max_length=30, default='#ffffff')
    line_separation = models.IntegerField(
        default=50, validators=[MinValueValidator(0), MaxValueValidator(100)])
    logo_path = models.ImageField(upload_to=f'logo', blank=True)
    logo_size = models.IntegerField(
        default=10, validators=[MinValueValidator(0), MaxValueValidator(100)])
    brightness = models.IntegerField(
        default=100, validators=[MinValueValidator(0), MaxValueValidator(100)])
    greyscale = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        if self.code == '':
            code = generate_ref_code()
            self.code = code
        super().save(*args, **kwargs)
