from django.contrib import admin

# Register your models here.

from .models import Downloads, Application

class DownloadsInline(admin.TabularInline):
    model = Downloads

class ApplicationAdmin(admin.ModelAdmin):
    # pass
    inlines=[DownloadsInline]

class DownloadsAdmin(admin.ModelAdmin):
    # pass
    list_display=['application', 'location', 'version']

admin.site.register(Application, ApplicationAdmin)
admin.site.register(Downloads, DownloadsAdmin)
