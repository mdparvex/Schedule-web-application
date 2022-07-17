from django.shortcuts import render, redirect
from django.contrib import messages
from .models import todo
from .forms import todoForms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView


# Create your views here.
@login_required
def index(request):
	if request.user.is_authenticated:
		item_list = todo.objects.filter(author=request.user).order_by("-date")


	page = {
		'list':item_list,
		'title':'TODO LIST',


	}
	return render(request, 'todo/index.html', page)


@login_required
def todoform(request):
	if request.method == 'POST':
		form = todoForms(request.POST)
		if form.is_valid():
			form = form.save(commit = False)
			form.author = request.user
			form.save()
			return redirect('todo')

	form = todoForms()

	return render(request, 'todo/todoform.html', {'forms':form})

@login_required
def remove(request, item_id):
	item = todo.objects.get(id=item_id)
	item.delete()
	messages.info(request, "item removed!!!!!")
	return redirect('todo')

	

''''
class PostCreateView(LoginRequiredMixin,CreateView):
	model= todo
	fields=['title', 'details', 'date']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

'''