from accounts.forms import SignUpForm
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render


def signup(request):
  if request.method == 'POST':
    form = SignUpForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data.get('username')
      raw_password = form.cleaned_data.get('password1')
      user = authenticate(username=username, password=raw_password)
      login(request, user)
      return redirect('home:home')
  else:
    form = SignUpForm()
  return render(request, 'accounts/signup.html', {'form': form})
