from django.contrib import admin
from .models import Subject,Video
from django.contrib.auth.admin import UserAdmin


class VideoAdmin(admin.ModelAdmin):
    list_display = ('subject','video_link','video_date')
    search_fields = ('subject__sub_name','video_date')
    filter_horizontal = ()
    ordering = ()
    list_filter = ()
    fieldsets = ()


# Register your models here.
admin.site.register(Subject)
admin.site.register(Video,VideoAdmin)