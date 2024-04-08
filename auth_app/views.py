from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # This seems incorrect, it should probably be a redirect or render of another page
            return 'success'
    else:
        form = UserCreationForm()
    return render(request, 'auth/register.html', {'form': form})


def login_view(request):
    pass


def dashboard(request):
    pass


def logout(request):
    pass
