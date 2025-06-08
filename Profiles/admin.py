from django.contrib import admin
from .models import CustomUser, Profile

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'date_joined')
    search_fields = ('email', 'username')
    ordering = ('-date_joined',)
    
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio',)
    search_fields = ('user__email', 'user__username')
    ordering = ('user__date_joined',)
    

