from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *

import hashlib
import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet


def generate_key(password_provided):
    password = password_provided.encode()
    salt = b'Do\xdbw>\xc4\x99\xea/\xc4~j\xe2\x86\x16M'
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt,
                     iterations=100000, backend=default_backend())

    key = base64.urlsafe_b64encode(kdf.derive(password))
    return key.decode()


def encrypt(message, key):
    f = Fernet(key)
    encrypted = f.encrypt(message.encode())
    return encrypted.decode()


def decrypt(encrypted, key):
    f = Fernet(key)
    decrypted = f.decrypt(encrypted)
    return decrypted.decode()

@login_required
def create(request):
    if request.user.masterpassword.master == '':
        return redirect('master')

    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            key = form.cleaned_data['key']
            key = generate_key(key)

            crypt = hashlib.sha256()
            crypt.update(key.encode())
            key = crypt.hexdigest()
            print(key)
            print(request.user.masterpassword.master)

            if key[0:3] == request.user.masterpassword.master:

                site_password_used = form.cleaned_data['site_password_used']
                key = generate_key(form.cleaned_data['key'])
                site_password = encrypt(message=site_password_used, key=key)
                print('site password ->', site_password)

                entry = Entry.objects.create(author=request.user, site_name=form.cleaned_data['site_name'],
                                             site_email_used=form.cleaned_data['site_email_used'], site_password_used=site_password)

                # form.save()
                entry.save()
                messages.success(
                    request, f'A new entry was successfully added.')
                return redirect('entry-create')
            else:
                messages.warning(request, f'Your master passeword is wrong.')
                form = EntryForm(request.POST)
                return render(request, 'passwordsmanager/create.html', {'form': form})
    form = EntryForm()
    return render(request, 'passwordsmanager/create.html', {'form': form})


@login_required
def master(request):
    if request.method == 'POST':
        form = MasterPasswordForm(
            request.POST, instance=request.user.masterpassword)

        if form.is_valid():

            key = form.cleaned_data['master']
            key2 = form.cleaned_data['master_confirm']
            last_master = form.cleaned_data['last_master']
            last_master2 = generate_key(last_master)
            crypt = hashlib.sha256()
            crypt.update(last_master2.encode())
            last_master2 = crypt.hexdigest()

            if MasterPassword.objects.get(author=request.user).master != '':

                print('last master: ',last_master2[0:3])
                print('request.user.masterpassword.master: ', MasterPassword.objects.get(author=request.user).master)

                if last_master2[0:3] != MasterPassword.objects.get(author=request.user).master:
                    messages.warning(request, 'The last master password you typed is wrong. Let it blank if it the first time creating one.')
                    return render(request, 'passwordsmanager/master.html', {'form': form})


            if key != key2:
                messages.warning(request, 'Fields Master Password and master password confirm do not match')
                return render(request, 'passwordsmanager/master.html', {'form': form})

            key = generate_key(key)
            last_master = generate_key(last_master)

            obj = form.save(commit=False)
            password = form.cleaned_data['master']
            password = generate_key(password)


            entries = Entry.objects.filter(author=request.user)

            for entry in entries:
                entry.site_password_used = decrypt(encrypted=entry.site_password_used.encode() ,key=last_master.encode())
                print(entry.site_password_used)
                entry.site_password_used = encrypt(message=entry.site_password_used, key=key.encode())
                print(entry.site_password_used)
                entry.save()

            crypt = hashlib.sha256()
            crypt.update(password.encode())
            password = crypt.hexdigest()
            obj.master = password[0:3]
            obj.save()

            messages.success(
                request, f'Your Master Password was successfully edited.')
            return redirect('entry-create')
        else:
            return render(request, 'passwordsmanager/master.html', {'form': form})

    form = MasterPasswordForm()
    return render(request, 'passwordsmanager/master.html', {'form': form})


@login_required
def showpasswords(request):
    if request.method == 'POST':
        form = MasterForm(request.POST)
        if form.is_valid():
            key = form.cleaned_data['key']
            key = generate_key(key)

            crypt = hashlib.sha256()
            crypt.update(key.encode())
            key2 = crypt.hexdigest()

            if key2[0:3] == MasterPassword.objects.get(author=request.user).master:
                entries = Entry.objects.filter(author=request.user)

                for entry in entries:
                    entry.site_password_used = decrypt(encrypted=entry.site_password_used.encode() ,key=key.encode())

                return render(request, 'passwordsmanager/show.html', {'entries': entries})
            else:
                messages.warning(request, f'Your master passeword is wrong.')
                return render(request, 'passwordsmanager/master.html', {'form': form})


    form = MasterForm()
    return render(request, 'passwordsmanager/master.html', {'form': form})

def home(request):
    return render(request, 'passwordsmanager/index.html')


def delete(request, pk):
    entry = Entry.objects.get(pk=pk)
    if request.method == 'POST':
        entry.delete()
        print('Deleted')
        return redirect('mypasswords')
    return render(request, 'passwordsmanager/delete.html', {'entry': entry})
