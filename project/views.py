from django.shortcuts import render, get_object_or_404
from project.models import Project


def all_projects(request):
    projects = Project.objects.all()
    return render(request, 'project/all_projects.html', {'projects': projects})


def project_detail(request, project_id):
    detail = get_object_or_404(Project, pk=project_id)
    return render(request, 'project/project_detail.html', {'detail': detail})
