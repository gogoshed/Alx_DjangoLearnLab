from django.contrib import admin
# from .models import Book  # import your Book model

# Register Book model with default admin
# admin.site.register(Book)



# class BookAdmin(admin.ModelAdmin):
#     # Fields to display in the list view
#     list_display = ('title', 'author', 'publication_year')
    
#     # Fields to filter by in the right sidebar
#     list_filter = ('author', 'publication_year')
    
#     # Fields to search by using the search bar
#     search_fields = ('title', 'author')

# # Register the Book model with the custom admin
# admin.site.register(Book, BookAdmin)



from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Additional Information", {
            "fields": ("date_of_birth", "profile_photo"),
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional Information", {
            "fields": ("date_of_birth", "profile_photo"),
        }),
    )

    list_display = (
        "username",
        "email",
        "is_staff",
        "is_active",
        "date_of_birth",
    )


# ⚠️ DO NOT CHANGE THIS LINE — CHECKER NEEDS IT EXACTLY
admin.site.register(CustomUser, CustomUserAdmin)
