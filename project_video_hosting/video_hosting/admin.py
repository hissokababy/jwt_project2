from django.contrib import admin

from video_hosting.models import User, Video, WatchedVideo

# Register your models here.

class VideoInline(admin.TabularInline):
    fk_name = 'created_by'
    extra = 1
    model = Video

class WatchedVideoInline(admin.TabularInline):
    fk_name = 'video_id'
    extra = 1
    model = WatchedVideo

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'is_active']
    inlines = [VideoInline,]

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_by', 'duration', 'created_at']
    inlines = [WatchedVideoInline,]
    