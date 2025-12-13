from urllib import request
from django.shortcuts import render

# Create your views here.
def index(request):
     return render(request, "idcardapp/index.html")

from django.shortcuts import render, redirect
from .models import Department, Employee
from django.contrib.auth import get_user_model

User = get_user_model()

def add_employee(request):
    departments = Department.objects.all()

    if request.method == "POST":
        department_id = request.POST.get("department")

        if not department_id:
            return render(
                request,
                "add_employee.html",
                {
                    "departments": departments,
                    "error": "Please select a department"
                }
            )

        user = User.objects.create_user(
            email=request.POST.get("email"),
            password="Employee@123"
        )

        Employee.objects.create(
            user=user,
            full_name=request.POST.get("full_name"),
            phone=request.POST.get("phone"),
            department_id=department_id,
            position=request.POST.get("position"),
            profile_photo=request.FILES.get("profile_photo")
        )

        return redirect("add_employee")

    return render(request, "add_employee.html", {"departments": departments})

# print(request.POST)

from django.shortcuts import render, redirect
from .forms import DepartmentForm

def add_department(request):
    if request.method == "POST":
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("add_department")
    else:
        form = DepartmentForm()

    return render(request, "add_department.html", {"form": form})


from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee, Department
from django.contrib.auth import get_user_model

User = get_user_model()

def employee_list(request):
    employees = Employee.objects.select_related("department", "user")
    return render(request, "employee_list.html", {"employees": employees})


def update_employee(request, emp_id):
    employee = get_object_or_404(Employee, emp_id=emp_id)
    departments = Department.objects.all()

    if request.method == "POST":
        employee.full_name = request.POST.get("full_name")
        employee.phone = request.POST.get("phone")
        employee.position = request.POST.get("position")
        employee.department_id = request.POST.get("department")

        if request.FILES.get("profile_photo"):
            employee.profile_photo = request.FILES.get("profile_photo")

        # Update email (username)
        employee.user.email = request.POST.get("email")
        employee.user.save()

        employee.save()
        return redirect("employee_list")

    return render(
        request,
        "update_employee.html",
        {
            "employee": employee,
            "departments": departments
        }
    )



def delete_employee(request, emp_id):
    employee = get_object_or_404(Employee, emp_id=emp_id)

    if request.method == "POST":
        employee.user.delete()  # deletes employee also (CASCADE)
        return redirect("employee_list")

    return render(request, "delete_employee.html", {"employee": employee})



from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import AdminCreateForm

def is_admin(user):
    return user.is_superuser

@login_required
@user_passes_test(is_admin)
def add_admin(request):
    if request.method == "POST":
        form = AdminCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("admin_list")
    else:
        form = AdminCreateForm()

    return render(request, "add_admin.html", {"form": form})



from django.contrib.auth import authenticate, login

def user_login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, email=email, password=password)

        if user:
            login(request, user)
            return redirect("employee_list")
        else:
            return render(request, "login.html", {"error": "Invalid credentials"})

    return render(request, "login.html")


from django.contrib.auth import get_user_model

User = get_user_model()

def admin_list(request):
    admins = User.objects.filter(is_superuser=True)
    return render(request, "admin_list.html", {"admins": admins})
