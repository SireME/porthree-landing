from django.contrib import admin
from .models import PorthreeAbout, PorthreeFAQ

class PorthreeAboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at',
                    'updated_at', 'about',
                    'image')
class PorthreeFAQAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at',
                    'updated_at', 'question',
                    'answer')

# Register your models here.
admin.site.register(PorthreeAbout, PorthreeAboutAdmin)
admin.site.register(PorthreeFAQ, PorthreeFAQAdmin)
