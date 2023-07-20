from django.contrib import admin
from blogging.models import Post, Category

class CategoryInline(admin.TabularInline):
    model = Category.posts.through

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'text', 'created_date')
    fieldsets = (
        ('Posts', {
            'fields': ('title', 'author', 'text')
        }),
        )
    inlines = [CategoryInline]


class CategoryAdmin(admin.ModelAdmin):
    exclude = ('posts',)

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)

