from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from applicant.models import Applicant
from applicant.forms.applicant_form import ApplicantForm



# Create your views here.


def applicant(request):
    applicant = Applicant.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = ApplicantForm(instance=applicant, data=request.POST)
        if form.is_valid():
            applicant = form.save(commit=False)
            applicant.user = request.user
            applicant.save()
            return redirect('applicant')
    return render(request, 'applicant/applicant.html', {
        'form': ApplicantForm(instance=applicant) 
    })

def index(request):
    applicant = Applicant.objects.filter(user=request.user).first()
    return render(request,'applicant/index.html', {'applicant': applicant})
