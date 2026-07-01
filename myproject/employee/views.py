from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views import View
from django.contrib import messages
from .models import Employee

# ==========================================
# SLIDE 6 & 15: Function-Based Views (FBV)
# ==========================================
def simple_http_demo(request):
    """Slide 6 Demo: Direct HttpResponse"""
    return HttpResponse("<h1>Welcome to Django - Simple HttpResponse Demo</h1><p><a href='/employee/'>Go to Employee Portal</a></p>")

def home(request):
    """Slide 7 & 15 Demo: Rendering an HTML Template with Context"""
    # Slide 19: Check if session has stored user name
    user_name = request.session.get('visitor_name', 'John Doe')
    context = {
        'name': user_name,
        'total_employees': Employee.objects.count()
    }
    return render(request, 'employee/home.html', context)

# ==========================================
# SLIDE 16: Class-Based Views (CBV)
# ==========================================
class HomeView(View):
    """Slide 16 Demo: Reusable Class-Based View"""
    def get(self, request):
        context = {
            'name': 'Class-Based View User',
            'total_employees': Employee.objects.count()
        }
        return render(request, 'employee/home.html', context)

# ==========================================
# SLIDE 11, 14 & 23: CRUD Read & Search (GET vs POST)
# ==========================================
def employee_list(request):
    """Slide 14 & 23 Demo: ORM Read & Search"""
    search_query = request.GET.get('search', '')
    if search_query:
        # Slide 23: Search employee feature
        employees = Employee.objects.filter(name__icontains=search_query) | Employee.objects.filter(department__icontains=search_query)
    else:
        # Slide 12 & 14: ORM query all()
        employees = Employee.objects.all()
    
    return render(request, 'employee/list.html', {
        'employees': employees,
        'search_query': search_query
    })

# ==========================================
# SLIDE 10, 11 & 14: CRUD Create & Form Handling
# ==========================================
def employee_create(request):
    """Slide 10, 11 & 14 Demo: POST handling, CSRF token & ORM Create"""
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        department = request.POST.get('department', 'General').strip()
        salary = request.POST.get('salary', 50000)

        # Slide 10: Validation checks
        if not name or not email:
            messages.error(request, "Name and Email are required fields!")
            return render(request, 'employee/form.html', {'error': "Required fields missing."})

        try:
            # Slide 14: ORM Create
            Employee.objects.create(
                name=name,
                email=email,
                department=department,
                salary=salary
            )
            messages.success(request, f"Employee {name} created successfully!")
            return redirect('employee:list')
        except Exception as e:
            messages.error(request, f"Error creating employee: {str(e)}")
            return render(request, 'employee/form.html', {'error': str(e)})

    return render(request, 'employee/form.html', {'action': 'Create'})

# ==========================================
# SLIDE 14 & 23: CRUD Update
# ==========================================
def employee_update(request, pk):
    """Slide 14 & 23 Demo: ORM Update (emp.name = ... ; emp.save())"""
    emp = get_object_or_404(Employee, pk=pk)
    
    if request.method == 'POST':
        emp.name = request.POST.get('name', emp.name)
        emp.email = request.POST.get('email', emp.email)
        emp.department = request.POST.get('department', emp.department)
        emp.salary = request.POST.get('salary', emp.salary)
        
        # Slide 14: Save updated object
        emp.save()
        messages.success(request, f"Employee {emp.name} updated successfully!")
        return redirect('employee:list')

    return render(request, 'employee/form.html', {'employee': emp, 'action': 'Update'})

# ==========================================
# SLIDE 14 & 23: CRUD Delete
# ==========================================
def employee_delete(request, pk):
    """Slide 14 & 23 Demo: ORM Delete (emp.delete())"""
    emp = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        emp_name = emp.name
        # Slide 14: Delete record
        emp.delete()
        messages.success(request, f"Employee {emp_name} deleted successfully!")
        return redirect('employee:list')
    
    return render(request, 'employee/delete_confirm.html', {'employee': emp})

# ==========================================
# SLIDE 19: Session Management Demo
# ==========================================
def session_demo(request):
    """Slide 19 Demo: Session Stores (request.session['key'] = value)"""
    if request.method == 'POST':
        visitor_name = request.POST.get('visitor_name', 'Guest')
        # Set session value
        request.session['visitor_name'] = visitor_name
        messages.info(request, f"Session value saved as: {visitor_name}")
        return redirect('employee:session_demo')
    
    current_session_val = request.session.get('visitor_name', 'None set')
    return render(request, 'employee/session_demo.html', {'current_session_val': current_session_val})
