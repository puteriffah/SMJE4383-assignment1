from django.shortcuts import render, redirect
from todo_list.models import List
from todo_list.forms import ListForm
from django.contrib import messages

def home(request):
	if request.method == 'POST':
		form = ListForm(request.POST or None)

		if form.is_valid():
			form.save()
			all_items = List.objects.all
			messages.success(request, ('List updated!'))
			return render(request, 'home.html', {'all_items': all_items})

	else:
		all_items = List.objects.all
		return render(request, 'home.html', {'all_items': all_items})

def delete(request, list_id):
	item = List.objects.get(pk = list_id)
	item.delete()
	messages.success(request, ('Successfully deleted!'))
	return redirect('HOMEPAGE')

def cross_off(request, list_id):
	item = List.objects.get(pk = list_id)
	item.completed = True
	item.save()
	return redirect('HOMEPAGE')

def uncross(request, list_id):
	item = List.objects.get(pk = list_id)
	item.completed = False
	item.save()
	return redirect('HOMEPAGE')
