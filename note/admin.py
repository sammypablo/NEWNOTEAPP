from django.contrib import admin
from .models import Note

class NoteAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'title', 'created_at']
    list_filter = ['user', 'created_at', 'title']
    search_fields = ['id', 'user', 'title', 'created_at']
    readonly_fields = ['id', 'created_at']


admin.site.register(Note, NoteAdmin)

