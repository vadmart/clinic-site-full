from django.shortcuts import render
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, template_name="clinic/index.html", context={})


def staff(request):
    return render(request, template_name="clinic/pages/staff.html", context={})
