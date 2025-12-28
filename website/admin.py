from django.contrib import admin
from .models import ContactMessage, GalleryImage, SchoolInfo

# Register your models here.
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject_snippet', 'created_at')
    search_fields = ('name', 'email', 'message')
    list_filter = ('created_at',)
    readonly_fields = ('created_at',)

    def subject_snippet(self, obj):
        return obj.message[:50] + '...' if len(obj.message) > 50 else obj.message
    subject_snippet.short_description = 'Message'

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'description')

@admin.register(SchoolInfo)
class SchoolInfoAdmin(admin.ModelAdmin):
    list_display = ('name','vision','mission','created_at')
    search_fields = ('name', 'vision', 'mission')
    
    def has_add_permission(self, request):
        # Allow only one instance
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)

