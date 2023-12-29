from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from django.contrib.auth.admin import UserAdmin as BAseUserAdmin
from tags.models import TaggedItem
from store.admin import ProductAdmin
from store.models import Product
from core.models import User

@admin.register(User)
class UserAdmin(BAseUserAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2", "email", "first_name", "last_name"),
            },
        ),
    )
    # pass
    

class TagItemInline(GenericTabularInline):
    autocomplete_fields = ['tag']
    model = TaggedItem
    min_num = 1
    max_num = 5
    extra = 0
    
class CustomProductAdmin(ProductAdmin):
    inlines = [TagItemInline]
    
admin.site.unregister(Product)
admin.site.register(Product, CustomProductAdmin)

