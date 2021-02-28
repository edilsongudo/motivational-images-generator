from django.shortcuts import render, redirect
from django.http import FileResponse, JsonResponse
from .forms import UserProfileForm, UserRegisterForm
from .models import Profile
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.utils.safestring import mark_safe
from django.utils.html import format_html
from .creator.randompost import Posts
import os, random, json

def delete(path, file_limit_ammount=100, ignore=''):
    try:
        folder = os.listdir(os.path.join(settings.BASE_DIR, path))
        if len(folder) >= file_limit_ammount:
            for item in folder:
                if folder[-1] != item:
                    os.remove(os.path.join(settings.BASE_DIR, f'{path}/{item}'))
                    print('Item deleted')
                else:
                    print('This is the last item')
    except Exception as e:
        print(e)


def index(request, *args, **kwargs):
    try:
        code = str(kwargs.get('ref_code'))
        profile = Profile.objects.get(code=code)

        if request.user != profile.user: #Handle clicks
            # if str(request.session['ref_code']) != str(profile.id):
            profile.ref_code_clicks += 1
            profile.save()

        request.session['ref_code'] = profile.id
        print(f'Refferal: {profile.user.username}')
    except Exception as e:
        print(e)
    if request.user.is_authenticated:
        return render(request, 'posts/index.html') #return landing page not this
    return render(request, 'posts/home.html')


@login_required
def download(request, image):
    delete('media/images/download')
    if request.user.profile.connects > 0:
        if request.user.profile.last_image_downloaded != image:
            request.user.profile.last_image_downloaded = image
            request.user.profile.connects -= 1
            request.user.profile.number_of_posts_downloaded += 1
            request.user.profile.save()
        mediaroot = settings.MEDIA_ROOT
        return FileResponse(open(os.path.join(mediaroot, f'images/download/{image}'), 'rb'))
    else:
        # messages.warning(request, format_html(f'<a target="_blank" href="{request.get_host()}/checkout">You have no more credits. You can get more here.</a>'))
        return redirect('posts-create')


@login_required
def create(request):
    request.user.profile.number_of_posts_created += 1
    request.user.profile.save()
    delete('media/images/created')
    mediaroot = settings.MEDIA_ROOT
    try:
        logo_path = f'{settings.BASE_DIR}{request.user.profile.logo_path.url}'
    except:
        logo_path = ''
    color = request.user.profile.primary_text_color
    greyscale = request.user.profile.greyscale
    secondary_text = request.user.profile.brand_name
    line_sep = request.user.profile.line_separation
    logo_size = request.user.profile.logo_size
    primary_font_size = request.user.profile.primary_font_size
    primary_font_type = request.user.profile.primary_font_type
    secondary_font_size = request.user.profile.brand_name_font_size
    brightness = request.user.profile.brightness
    secondary_font_size = request.user.profile.brand_name_font_size
    brand_name_font_color = request.user.profile.brand_name_font_color
    brand_name_font_type = request.user.profile.brand_name_font_type

    secondary_font_size = secondary_font_size / 50
    primary_font_size = primary_font_size / 50
    line_sep = line_sep / 50
    logo_size = logo_size / 10
    brightness = brightness / 300
    # logo_color

    fonts = os.listdir(os.path.join(settings.MEDIA_ROOT, 'fonts'))
    for font in fonts:
        if primary_font_type == font.split('.')[0]:
            primary_font_type = font
        if brand_name_font_type == font.split('.')[0]:
            brand_name_font_type = font

    if 'En' in request.user.profile.language:
        texts = []
        files = os.listdir(os.path.join(settings.BASE_DIR, f'posts/creator/Texts/English'))
        for file in files:
            with open(os.path.join(settings.BASE_DIR, f'posts/creator/Texts/English/{file}'), 'r') as file:
                phrases = file.readlines()
                for phrase in phrases:
                    texts.append(phrase)
        text = random.choice(texts)
    elif 'ortugu' in request.user.profile.language:
        texts = []
        files = os.listdir(os.path.join(settings.BASE_DIR, f'posts/creator/Texts/Portugues'))
        for file in files:
            with open(os.path.join(settings.BASE_DIR, f'posts/creator/Texts/Portugues/{file}'), 'r') as file:
                phrases = file.readlines()
                for phrase in phrases:
                    texts.append(phrase)
        text = random.choice(texts)


    bot = Posts()
    post = bot.createPost(
        text=text, color=color, color2=brand_name_font_color, primary_font_type=primary_font_type,
        logo_path=logo_path, logo_size=logo_size, secondary_font_size=secondary_font_size,
        primary_font_size=primary_font_size, line_sep=line_sep, secondary_text=secondary_text,
        greyscale=greyscale, dim_factor=brightness, secondary_font_type=brand_name_font_type
    )

    if request.is_ajax():
        return JsonResponse({'response': post, 'credits': request.user.profile.connects, 'siteurl': request.get_host()})
    return render(request, 'posts/posts_create.html', {'media_url': mediaroot, 'post': post, 'title': 'Create Posts'})


@login_required
def profile(request):
    if request.is_ajax():
        data = json.loads(request.body)
        color = data['primary_text_color']
        primary_font_type = data['primary_font_type']
        primary_font_size = int(data['primary_font_size'])
        brand_name = data['brand_name']
        brand_name_font_type = data['brand_name_font_type']
        brand_name_font_size = int(data['brand_name_font_size'])
        brand_name_font_color = data['brand_name_font_color']
        logo_size = int(data['logo_size'])
        brightness = int(data['brightness'])
        greyscale = data['greyscale']
        if greyscale == 'true':
            greyscale = True
        line_separation = int(data['line_separation'])

        brand_name_font_size = brand_name_font_size / 50
        primary_font_size = primary_font_size / 50
        line_separation = line_separation / 50
        logo_size = logo_size / 10
        brightness = brightness / 300

        delete('media/images/temp/preview')

        fonts = os.listdir(os.path.join(settings.MEDIA_ROOT, 'fonts'))
        for font in fonts:
            if primary_font_type == font.split('.')[0]:
                primary_font_type = font
            if brand_name_font_type == font.split('.')[0]:
                brand_name_font_type = font

        bot = Posts()
        text = 'You can preview your changes here.'
        logo_path=''
        post = bot.createPost(
            text=text, color=color, color2=brand_name_font_color, primary_font_type=primary_font_type,
            logo_path=logo_path, logo_size=logo_size, secondary_font_size=brand_name_font_size,
            primary_font_size=primary_font_size, line_sep=line_separation, secondary_text=brand_name,
            greyscale=greyscale, dim_factor=brightness, secondary_font_type=brand_name_font_type, preview=True, username=request.user.username)

        return JsonResponse({"response": post})

    if request.method == 'POST':
        form = UserProfileForm(
            request.POST, request.FILES, instance=request.user.profile)  # request.FILES

        if form.is_valid():
            form.save()
            messages.success(request, f'Your preferences has been updated!')
            return redirect('posts-create')

    else:
        form = UserProfileForm(instance=request.user.profile)

    context = {
        'form': form,
        'title': 'Preferences'
    }


    mediaroot = settings.MEDIA_ROOT
    try:
        logo_path = f'{settings.BASE_DIR}{request.user.profile.logo_path.url}'
    except:
        logo_path = ''
    color = request.user.profile.primary_text_color
    greyscale = request.user.profile.greyscale
    secondary_text = request.user.profile.brand_name
    line_sep = request.user.profile.line_separation
    logo_size = request.user.profile.logo_size
    primary_font_size = request.user.profile.primary_font_size
    primary_font_type = request.user.profile.primary_font_type
    secondary_font_size = request.user.profile.brand_name_font_size
    brightness = request.user.profile.brightness
    secondary_font_size = request.user.profile.brand_name_font_size
    brand_name_font_color = request.user.profile.brand_name_font_color
    brand_name_font_type = request.user.profile.brand_name_font_type

    secondary_font_size = secondary_font_size / 50
    primary_font_size = primary_font_size / 50
    line_sep = line_sep / 50
    logo_size = logo_size / 10
    brightness = brightness / 300
    # logo_color

    fonts = os.listdir(os.path.join(settings.MEDIA_ROOT, 'fonts'))
    for font in fonts:
        if primary_font_type == font.split('.')[0]:
            primary_font_type = font
        if brand_name_font_type == font.split('.')[0]:
            brand_name_font_type = font

    bot = Posts()
    text = 'This is how your posts will look like.'
    post = bot.createPost(
        text=text, color=color, color2=brand_name_font_color, primary_font_type=primary_font_type,
        logo_path=logo_path, logo_size=logo_size, secondary_font_size=secondary_font_size,
        primary_font_size=primary_font_size, line_sep=line_sep, secondary_text=secondary_text,
        greyscale=greyscale, dim_factor=brightness, secondary_font_type=brand_name_font_type,
    preview=True, username=request.user.username)

    return render(request, 'posts/user_preferences.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')

            #referral system
            profile_id = request.session.get('ref_code')
            if profile_id is not None:
                print(profile_id)
                user = User.objects.get(username=username)
                user.profile.recommended_by = Profile.objects.get(id=profile_id).user
                user.profile.save()
                print('Refferal saved for this user')
            else:
                print('No referral found.')

            messages.success(
                request, f'Your Account has been created. You are now able to login.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'posts/register.html', {'form': form, 'title': 'Register'})


@login_required
def recommended_by_user(request):
    profiles = Profile.objects.all()
    recommended_by_user = []
    for profile in profiles:
        if profile.recommended_by == request.user:
            recommended_by_user.append(profile)
    print(recommended_by_user)
    return render(request, 'posts/recommended_by_user.html', {'profiles': recommended_by_user, 'title': 'My recomendations'})

@login_required
def affiliate_dashboard(request):
    return render(request, 'posts/affiliate_dashboard.html', {'profiles': recommended_by_user, 'domain': settings.ALLOWED_HOSTS[-1]})

@login_required
def checkout(request):
    user = request.user
    context = {'user': user, 'title': 'Checkout'}
    return render(request, 'posts/checkout.html', context)

@login_required
def paymentComplete(request):
    body = json.loads(request.body)
    print('BODY:', body)
    user = User.objects.get(pk=body['userId'])
    user.profile.connects += body['total'] * 8
    user.profile.save()
    messages.success(
    request, f'You now have {user.profile.connects} credits. Thank you for choosing our service:)')
    try:
        recommended_by = user.profile.recommended_by
        recommended_by.profile.money += body['total'] / 2
        recommended_by.profile.save()
    except Exception as e:
        print(e)
    return JsonResponse('Payment completed!', safe=False)
