from blog.models import Entry
from django.contrib import admin

class EntryAdmin(admin.ModelAdmin):
    model = Entry
    list_display = ("title","body")

admin.site.register(Entry,EntryAdmin)