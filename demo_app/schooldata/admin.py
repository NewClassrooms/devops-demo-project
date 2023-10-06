from django.contrib import admin

from .models import GradeLevel, Skill, School


@admin.register(GradeLevel)
class GradeLevelAdmin(admin.ModelAdmin):
    list_display = ['name', 'grade_level']


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'grade_level', 'difficulty']
    list_select_related = ['grade_level']
    search_fields = ['name']
    list_filter = ['grade_level']


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ['name']
