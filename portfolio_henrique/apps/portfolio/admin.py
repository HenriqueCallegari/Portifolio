"""
Registro dos models no Django Admin.
Acesse /admin/ após criar um superuser com:
    python manage.py createsuperuser
"""

from django.contrib import admin
from .models import Skill, Experience, Project


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display  = ("name", "category", "level", "order")
    list_filter   = ("category",)
    list_editable = ("level", "order")
    ordering      = ("category", "order")


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display  = ("role", "company", "exp_type", "start_date", "is_current")
    list_filter   = ("exp_type", "is_current")
    ordering      = ("-start_date",)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display   = ("title", "status", "featured", "order")
    list_editable  = ("featured", "order")
    list_filter    = ("status", "featured")
    prepopulated_fields = {"slug": ("title",)}  # preenche slug automaticamente
