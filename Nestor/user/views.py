from django.shortcuts import render, redirect
from django.contrib import messages
from user.forms.user_form import UserForm
from applicant.models import Applicant
from django.contrib.auth import login


def register(request):
    if request.method == 'POST':
        form = UserForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            # Creating applicant model for that user
            Applicant.objects.create(user=user)
            applicant = Applicant.objects.get(user=user)
            applicant.full_name = user.get_full_name()
            applicant.email = user.email
            applicant.save()
            login(request, user)

            return redirect('/')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field}: {error}')
    return render(request, 'user/register.html', {
        'form': UserForm(),
    })

