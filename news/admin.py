from django.contrib import admin

# Register your models here.
from news.models import *
from .form import SocialSidebarForm
 
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'category']
    prepopulated_fields = {'url':('title',)}

admin.site.register(News, NewsAdmin) 

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'url']
    prepopulated_fields = {'url':('name',)}
 
admin.site.register(Category, CategoryAdmin)

class SocialSidebarAdmin(admin.ModelAdmin):
    form = SocialSidebarForm
    list_display = ['link_address', 'social_name']
    prepopulated_fields = {'social_name':('link_address',)}

    fieldsets = (
        (None, {
            'fields': ('link_address', 'social_name', 'icon', 'background')
            }),
        )

admin.site.register(SocialSidebar, SocialSidebarAdmin)

class ContactsUsAdmin(admin.ModelAdmin):
    fieldsets = (
    (None, {
        'fields': ('our_office', 'email_us', 'call_us')
        }),
    )

admin.site.register(Contacts_us, ContactsUsAdmin)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'comm', 'post', 'created')
    search_fields = ('user_name', 'post', 'comm')

admin.site.register(Comment, CommentAdmin)