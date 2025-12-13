from django.urls import include
from django.contrib import admin
from django.urls import path, include
from idcardapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
#   path("", views.index, name="index"),
  path("add-employee/", views.add_employee, name="add_employee"),
  path("add-department/", views.add_department, name="add_department"),
  path("department/edit/<int:dept_id>/", views.edit_department, name="edit_department"),
  path("department/delete/<int:dept_id>/", views.delete_department, name="delete_department"),
  path("employees/", views.employee_list, name="employee_list"),
  path("employees/update/<int:emp_id>/", views.update_employee, name="update_employee"),
  path("employees/delete/<int:emp_id>/", views.delete_employee, name="delete_employee"),
  path("add-admin/", views.add_admin, name="add_admin"),
  path("login/", views.user_login, name="login"),
  path("admins/", views.admin_list, name="admin_list"),
  path("id-card/", views.id_card_list, name="id_card_list"),
  path("id-card/<int:emp_id>/", views.generate_id_card, name="generate_id_card"),
  path("", views.dashboard, name="dashboard"),



]