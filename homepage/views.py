from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.utils.translation import gettext as _
from django.utils import translation
from django.http import HttpResponseRedirect
from django.conf import settings

def set_language(request):
    user_language = request.POST.get('language', 'en')
    translation.activate(user_language)
    request.session[settings.LANGUAGE_SESSION_KEY] = user_language
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))



def my_view(request):
    languages = ['en', 'fr']
    translation.activate(languages[0])  # Activate the desired language
    #greeting = _("Welcome")
    return render(request, 'index1.html')


def home(request):
    return render(request=request, template_name="index1.html")

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save the contact to the database
            return redirect('success')  # Redirect after success
    else:
        form = ContactForm()

    return render(request, 'index1.html', {'form': form})


def contact_success(request):
    return render(request, 'success.html')  # Create a success template
