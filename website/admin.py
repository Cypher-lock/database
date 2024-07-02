from django.contrib import admin
from .models import Softmatterdata

# Register your models here.
#admin.site.register(Softmatterdata)

@admin.register(Softmatterdata)
class SoftmatterdataAdmin(admin.ModelAdmin):
    fields = ('composition', 'method', 'name', ('acquired'), ('doi', 'summary'), ('sample_image', 'meta_data'))
    list_display = ('composition', 'method', 'name', 'acquired', 'lastupdate', 'doi', 'summary', 'sample_image', 'meta_data')
    ordering = ('name',)
    search_fields = ('name', 'composition', 'method', 'summary')