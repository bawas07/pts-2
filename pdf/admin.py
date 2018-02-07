from django.contrib import admin

from pdf.models import *
from pdf.list_filter import *
# Register your models here.
class CoreAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ()
    search_fields = ['name']
    list_per_page = 25

admin.site.register(Core, CoreAdmin)

class StageAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ()
    search_fields = ['name']
    list_per_page = 25

admin.site.register(Stage, StageAdmin)

class FrameworkAdmin(admin.ModelAdmin):
    list_display = ['name', 'core']
    list_filter = ('core',)
    search_fields = ['name']
    list_per_page = 25

admin.site.register(Framework, FrameworkAdmin)

class IndicatorAdmin(admin.ModelAdmin):
    list_display = ['name', 'core', 'framework', 'stage']
    list_filter = ('framework__core', FrameworkListFilter, 'stage',)
    search_fields = ['name']
    list_per_page = 25

    def core(self, obj):
        return obj.framework.core

admin.site.register(Indicator, IndicatorAdmin)

class CoreDescAdmin(admin.ModelAdmin):
    list_display = ['descriptor', 'stage', 'core']
    list_filter = ('stage', 'core',)
    search_fields = ['descriptor']
    list_per_page = 25

admin.site.register(CoreDesc, CoreDescAdmin)

class FrameworkDescAdmin(admin.ModelAdmin):
    list_display = ['descriptor', 'stage', 'framework']
    list_filter = ('stage', 'framework',)
    search_fields = ['descriptor']
    list_per_page = 25

admin.site.register(FrameworkDesc, FrameworkDescAdmin)