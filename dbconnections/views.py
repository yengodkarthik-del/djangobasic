from django.shortcuts import render
from.models import register
from.forms import registerform   

# Create your views here.
def register(request):
    form = registerform(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("register")
    return render(request, "register.html", {"form": form})
