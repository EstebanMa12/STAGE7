from django.contrib import admin

# models
from posts.models import Post


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Post admin"""
    list_display = ('id','user','title','photo','created','modified')
    list_display_links = ('id','title')
    search_fields = (
        'title',
        'user__username',
        'user__email',
        'profile__user__username',
        'profile__user__email'
    )
    list_filter = (
        'created',
        'modified'
    )
    fieldsets = (
        ('Post',{
            'fields':(
                ('title','photo'),
            )
        }),
        ('Metadata',{
            'fields':(
                ('created','modified'),
            )
        })
    )
    readonly_fields = ('created','modified')