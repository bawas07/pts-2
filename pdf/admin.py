from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models

from pdf.models import *
from pdf.list_filter import *
# Register your models here.
class CoreDescInline(admin.TabularInline):
    model = CoreDesc
    extra = 0
    classes = ('grp-collapse grp-open',)
#    show_change_link = True
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 1, 'cols': 150})},
    }

class FrameworkInline(admin.TabularInline):
    model = Framework
    extra = 0
    classes = ('grp-collapse grp-open',)
#    show_change_link = True
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 1, 'cols': 150})},
    }

class CoreAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ()
    search_fields = ['name']
    list_per_page = 25
    inlines = [CoreDescInline, FrameworkInline]

admin.site.register(Core, CoreAdmin)

class StageAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ()
    search_fields = ['name']
    list_per_page = 25

admin.site.register(Stage, StageAdmin)

class FrameDescInline(admin.TabularInline):
    model = FrameworkDesc
    extra = 0
    show_change_link = True
    classes = ('grp-collapse grp-open',)
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 1, 'cols': 150})},
    }

class IndicatorInline(admin.TabularInline):
    model = Indicator
    extra = 0
    show_change_link = True
    classes = ('grp-collapse grp-open',)
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 1, 'cols': 150})},
    }

class FrameworkAdmin(admin.ModelAdmin):
    list_display = ['name', 'core']
    list_filter = ('core',)
    search_fields = ['name']
    list_per_page = 25
    inlines = [FrameDescInline, IndicatorInline,]

admin.site.register(Framework, FrameworkAdmin)

class IndicatorAdmin(admin.ModelAdmin):
    list_display = ['name', 'core', 'framework', 'stage']
    list_filter = ('framework__core', FrameworkListFilter, 'stage',)
    search_fields = ['name']
    list_per_page = 25
    change_list_filter_template = "admin/filter_listing.html"
    change_list_template = "admin/change_list_filter_sidebar.html"

    def core(self, obj):
        return obj.framework.core

admin.site.register(Indicator, IndicatorAdmin)

class CoreDescAdmin(admin.ModelAdmin):
    list_display = ['descriptor', 'stage', 'core']
    list_filter = ('stage', 'core',)
    search_fields = ['descriptor']
    list_per_page = 25
    change_list_filter_template = "admin/filter_listing.html"
    change_list_template = "admin/change_list_filter_sidebar.html"

admin.site.register(CoreDesc, CoreDescAdmin)

class FrameworkDescAdmin(admin.ModelAdmin):
    list_display = ['descriptor', 'stage', 'framework']
    list_filter = ('framework__core', FrameworkListFilter, 'stage',)
    search_fields = ['descriptor']
    list_per_page = 25
    change_list_filter_template = "admin/filter_listing.html"
    change_list_template = "admin/change_list_filter_sidebar.html"

    def core(self, obj):
        return obj.framework.core

admin.site.register(FrameworkDesc, FrameworkDescAdmin)