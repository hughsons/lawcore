from django.contrib import admin
from models import Projects
from django.contrib.admin import SimpleListFilter
from django.contrib.admin import BooleanFieldListFilter

class ProjectsAdmin(admin.ModelAdmin):
    pass
    admin.site.register(Projects)
    