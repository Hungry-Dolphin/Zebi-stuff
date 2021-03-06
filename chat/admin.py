from django.contrib import admin
from .models import ChatRoom, ChatMessage, Profile


class ChatRoomAdmin(admin.ModelAdmin):
    ordering = ('-created_at',)
    list_filter = ['clearance', ]
    search_fields = ['name']
    list_display = ['name', 'clearance', 'id', 'created_at']


admin.site.register(ChatRoom, ChatRoomAdmin)


class ChatMessageAdmin(admin.ModelAdmin):
    ordering = ('-created_at',)
    list_display = ['send_in', 'created_at', 'user', 'content']
    search_fields = ['send_in__name', 'content', 'user__username']
    list_filter = ['send_in', ]


admin.site.register(ChatMessage, ChatMessageAdmin)


class ProfileAdmin(admin.ModelAdmin):
    ordering = ('-user',)
    list_display = ['user', 'clearance']
    search_fields = ['user__username']
    list_filter = ['clearance', ]


admin.site.register(Profile, ProfileAdmin)
