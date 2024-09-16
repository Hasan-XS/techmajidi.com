from django.contrib import admin
from .models import Post, Image, Blog, ImageBlog
# Register your models here.

# class ImageInline(admin.StackedInline):
#     model : Image
#     extra = 1

# class PostAdmin(admin.ModelAdmin):
#     inlines = [ImageInline]

#     list_display = ["title_image", "get_image_count"]

#     def get_image_count(self, obg):
#         return obg.images.count()
#     get_image_count.short_description = "some image"
    
admin.site.register(Post)
admin.site.register(Image)
admin.site.register(Blog)
admin.site.register(ImageBlog)
