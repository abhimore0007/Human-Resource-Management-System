from django.shortcuts import render,redirect
from .models import Role
from django.contrib import messages
from .forms import RoleForm
# Create your views here.

def add_roles(request):
    if request.method == 'POST':
        form = RoleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Role added successfully!")
            return redirect('dashboard')  
    else:
        form = RoleForm()

    return render(request, 'core/home.html', {'form': form})
