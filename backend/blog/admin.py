from django.contrib import admin
from .models import Post, Tag

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
  model = Tag

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
  model = Post

  list_display = (
    "id",
    "title",
    "slug",
    "published",
    "createdAt",
  )
  list_filter = (
    "published",
    "createdAt",
  )
  list_editable = (
    "title",
    "slug",
    "published",
  )
  search_fields = (
    "title",
    "slug",
    "body",
  )
  prepopulated_fields = {
    "slug": (
      "title",
    )
  }
  date_hierarchy = "createdAt"
  save_on_top = True
