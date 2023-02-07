from django.contrib import admin
from .models import Post, Profile, Tag

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
  model = Profile

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
    "publishedAt",
    "published",
  )
  list_filter = (
    "published",
    "publishedAt",
  )
  list_editable = (
    "title",
    "slug",
    "publishedAt",
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
  date_hierarchy = "publishedAt"
  save_on_top = True
