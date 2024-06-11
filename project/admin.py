from django.contrib import admin
from .models import Project, Tool


# Register your models here.
class ToolAdmin(admin.StackedInline):
    model = Tool
    extra = 1


class ProjectAdmin(admin.ModelAdmin):
    inlines = [ToolAdmin]


admin.site.register(Project, ProjectAdmin)
