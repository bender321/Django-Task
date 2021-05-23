from django.shortcuts import render, redirect
from django.contrib import messages
from .validators import IcoValidator, MailValidator
from .models import Entrepreneur
from . import forms


def index(request):

    redirected_url = 'index'

    if request.method == 'POST':

        form = forms.CreateEntrepreneur(request.POST)

        if form.is_valid():

            #check for if records with given parameters are already in app database

            if Entrepreneur.objects.filter(mail=form.cleaned_data.get('mail')).exists():

                messages.error(request, 'Záznam obsahující tento mail již existuje!')
                return redirect(redirected_url)

            elif Entrepreneur.objects.filter(ico=form.cleaned_data.get('ico')).exists():

                messages.error(request, 'Záznam obsahující toto IČO již existuje!')
                return redirect(redirected_url)

            else:
                #check for different return codes from validation functions
                #if everything is OK, form data will be saved into the database
                #otherwise redirect to same page (refresh) and proprient error message is send to user

                ico_validator = IcoValidator(form.cleaned_data.get('ico'))
                mail_validator = MailValidator(form.cleaned_data.get('mail'))
                validated_ico = ico_validator.validate_ico()
                validated_mail = mail_validator.validate_mail()

                if validated_ico == 3:
                    messages.error(request, 'ARES databaze je nedostupná, zadané IČO nelze ověřit, záznam nebude uložen!')
                    return redirect(redirected_url)

                elif validated_ico == 2:
                    messages.error(request, 'Špatný formát IČO! (Zadejte 8 číslic)')
                    return redirect(redirected_url)

                elif validated_ico == 1:
                    messages.error(request, 'Toto IČO neexistuje v ARES databázi!')
                    return redirect(redirected_url)

                if validated_mail == 1:
                    messages.error(request, 'Špatný formát emailu!')
                    return redirect(redirected_url)

                form.save()
                form = forms.CreateEntrepreneur()
                messages.error(request, 'Záznam uložen!')
    else:
        form = forms.CreateEntrepreneur()

    return render(request, 'ukol/create_Entrepreneur_form.html', {'form': form})
