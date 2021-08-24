from django.contrib import admin

from project.models import Project, Task


class ProjectTaskInline(admin.TabularInline):
    model = Task
    extra = 2


class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectTaskInline]


admin.site.register(Project, ProjectAdmin)
admin.site.register(Task)
