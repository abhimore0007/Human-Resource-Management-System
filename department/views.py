from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Department,Role,CustomUser
from .forms import DepartmentForm,RegisterForm
from django.shortcuts import render, redirect,get_object_or_404
from roles.models import Role

def register(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            reg = RegisterForm(request.POST)
            if reg.is_valid():
                reg.save()
                messages.success(request, 'Registration Successful!')
                return redirect('dashboard')  # Redirect to the dashboard after successful registration
            else:
                messages.error(request, 'Error in registration form. Please correct the errors below.')
        else:
            reg = RegisterForm()  # Initialize the form if the method is not POST

        return render(request, 'core/register.html', {'reg': reg})  # Render the registration form template
    else:
        messages.error(request, 'You are not authorized to view this page.')
        return redirect('home_page')  # Redirect to home if the user is not a superuser

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            if user.is_superuser:
                messages.success(request, 'Login successful. Welcome to the Dashboard!')
                return redirect('dashboard')  
            else:
                messages.success(request, 'Login successful. Welcome to the dashboard!')
                return redirect('user_dashboard') 
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'core/login.html')

def home_page(request):
    return render(request,'core/home_page.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('home_page')

@login_required
def dashboard(request):
    if not request.user.is_superuser:
        messages.error(request, 'Access restricted to administrators.')
        return redirect('login')
    departments = Department.objects.filter(status=True)
    roles = Role.objects.all()
    customuser = CustomUser.objects.all()

    return render(request, 'core/Admin_dashboard.html', {
        'departments': departments,
        'roles': roles,
        'customuser': customuser
    })

@login_required
def user_dashboard(request):
    
    user_data = Department.objects.filter(status=True)
    if not user_data.exists():
        messages.error(request, 'No data found for your account.')
        return redirect('login')  

    return render(request, 'core/user_dashboard.html', {'user_data': user_data})

@login_required
def add_department(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Department added successfully!')
            return redirect('add_department')
        else:
            messages.error(request, 'There was an error adding the department.')
    else:
        form = DepartmentForm()
    return render(request, 'core/add_depatment.html', {'form': form})

@login_required
def delete_department(request, id):
    department = get_object_or_404(Department, pk=id)
    if request.method == 'POST':
        department.status = False
        department.save()
        messages.success(request, f'Department "{department.name}" deactivated successfully.')
        return redirect('dashboard')
    return render(request, 'core/confirm_delete.html', {'department': department})

@login_required
def update_department(request, id):
    department = get_object_or_404(Department, pk=id)
    form = DepartmentForm(request.POST or None, instance=department)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, f'Department "{department.name}" updated successfully.')
        return redirect('dashboard')
    return render(request, 'core/update.html', {'form': form})
