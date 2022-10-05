
from django.contrib import admin

from mainapp import models as mainapp_models
from authapp import models

@admin.register(mainapp_models.News)
class NewsAdmin(admin.ModelAdmin):
    search_fields = ["title", "preambule", "body"]

@admin.register(mainapp_models.Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ["id", "get_course_name", "num", "title", "deleted"]
    ordering = ["-course__name", "-num"]
    list_per_page = 15
    list_filter = ["course", "created", "deleted"]
    actions = ["mark_deleted"]

    def get_course_name(self, obj):
        return obj.course.name
        
    get_course_name.short_description = ("Course")

    def mark_deleted(self, request, queryset):
        queryset.update(deleted=True)

    mark_deleted.short_description = ("Mark deleted")

@admin.register(models.CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ["id", "username", "email", "is_active", "date_joined"]
    ordering = ["-date_joined"]
