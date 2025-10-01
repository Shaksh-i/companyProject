from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Department

class DepartmentListView(ListView):
    model = Department
    template_name = 'departments/department_list.html'
    context_object_name = 'departments'

class DepartmentDetailView(DetailView):
    model = Department
    template_name = 'departments/department_detail.html'
    context_object_name = 'department'

class DepartmentCreateView(CreateView):
    model = Department
    fields = ['deptname', 'hod', 'location']
    template_name = 'departments/department_form.html'
    success_url = reverse_lazy('department_list')

class DepartmentUpdateView(UpdateView):
    model = Department
    fields = ['deptname', 'hod', 'location']
    template_name = 'departments/department_form.html'
    success_url = reverse_lazy('department_list')

class DepartmentDeleteView(DeleteView):
    model = Department
    template_name = 'departments/department_confirm_delete.html'
    context_object_name = 'department'
    success_url = reverse_lazy('department_list')
