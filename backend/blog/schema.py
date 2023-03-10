import graphene
from graphene_django import DjangoObjectType
from django.contrib.auth import get_user_model
from .models import Post, Tag

User = get_user_model()

class PostType(DjangoObjectType):
  class Meta:
   model = Post

class AuthorType(DjangoObjectType):
   class Meta:
      model = User

class TagType(DjangoObjectType):
  class Meta:
   model = Tag
   fields = ('id', 'name',)

class Query(graphene.ObjectType):
   posts    = graphene.List(PostType)
   tags     = graphene.List(TagType)
   authors  = graphene.List(AuthorType)
   post_by_slug      = graphene.Field(PostType, slug=graphene.String())
   posts_by_author   = graphene.List(PostType, author=graphene.String())
   posts_by_tag      = graphene.List(PostType, tag=graphene.String())

   def resolve_posts(self, info, **kwargs):
      return Post.objects.filter(published=True)

   def resolve_tags(self, info, **kwargs):
      return Tag.objects.all()
   
   def resolve_authors(self, info):
      return User.objects.all()
      
   def resolve_post_by_slug(self, info, slug):
      return Post.objects.get(slug=slug)
   
   def resolve_posts_by_author(self, info, author):
      return Post.objects.filter(author__user__username=author)
   
   def resolve_posts_by_tag(self, info, tag):
      return Post.objects.filter(tags__name=tag)




schema = graphene.Schema(query=Query)