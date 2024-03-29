from django.contrib import admin
from .models import Contact


# Register your models here to manage them through the Django admin interface
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    # Fields to be displayed in the list view
    list_display = ('name', 'email', 'subject', 'created_at')
    # Fields to search within the admin list view
    search_fields = ('name', 'email')
    # Make all fields read-only
    readonly_fields = ('name', 'email', 'subject', 'message', 'created_at')

    # Customize the form view in admin (optional)
    fieldsets = (
        (None, {
            'fields': ('name', 'email', 'subject', 'message', 'created_at')
        }),
    )

    # Disable adding and modifying contact messages through the admin
    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False
