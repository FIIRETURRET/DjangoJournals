from django.contrib import admin

from .models import Journal

# Register your models here.
class JournalAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')

admin.site.register(Journal, JournalAdmin)