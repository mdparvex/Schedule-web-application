from django.shortcuts import render, redirect
from .forms import UserResisterForm
from django.contrib import messages

# Create your views here.
def register(request):
	
	if request.method == 'POST':
		form=UserResisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Your account has been crated! You are now able to login')
			return redirect('login')
	else:
		form=UserResisterForm()
	return render(request, 'user/register.html', {'form': form})
