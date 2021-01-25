from django.contrib import admin
from blog.models import Blog
from certificate.models import Certificate
from project.models import Project

admin.site.register(Certificate)
admin.site.register(Blog)
admin.site.register(Project)
