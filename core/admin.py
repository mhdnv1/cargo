from django.contrib import admin
from core.models import *
from django.utils.safestring import mark_safe
# Register your models here.

class SectionInline(admin.TabularInline):
    model = Section
    extra = 1
    
    
@admin.register(Setting)
class SettingAdmin(admin.ModelAdmin):
    inlines = [SectionInline]

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    readonly_fields = ('get_image',)
    list_display = ('get_title','get_image')
    
    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="110"')
    
    def get_title(self,obj):
        return obj.__str__()

    
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    '''Admin View for Order'''

    list_display = ('id','phone','date','is_done')
    list_filter = ('is_done','date')
    readonly_fields = ('phone','date')
    search_fields = ('phone',)
    ordering = ('-date',)
    list_editable = ('is_done', )
    list_per_page = 10

admin.site.register(ServicePrice)
    
    