from django.contrib import admin

# Register your models here.

from .models import Human, Doodle, DoodleListing

class DoodleInline(admin.TabularInline):
    model = Doodle

class HumanAdmin(admin.ModelAdmin):
    pass
    inlines=[DoodleInline]

class DoodleAdmin(admin.ModelAdmin):
    pass

class DoodleListingAdmin(admin.ModelAdmin):
    list_display=['doodle', 'id', 'subject', 'cost', 'date_created']
    search_fields=['description']
    readonly_fields=['date_created']



admin.site.register(Human, HumanAdmin)
admin.site.register(Doodle, DoodleAdmin)
admin.site.register(DoodleListing, DoodleListingAdmin)
