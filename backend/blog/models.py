from django.db import models
from django.utils.translation import gettext as _
from django.conf import settings

# Create your models here.

class Tag(models.Model):
  name    = models.CharField(_("Tag Name"), max_length=50, unique=True)
  
  def __str__(self):
    return self.name  

class Profile(models.Model):
  user = models.OneToOneField(
    settings.AUTH_USER_MODEL,
    on_delete=models.PROTECT,
    )
  website = models.URLField(blank=True)
  bio     = models.CharField(max_length=240, blank=True)

  def __str__(self):
    return self.user.get_username()

class Post(models.Model):
  title           = models.CharField(_("Title"), max_length=50, unique=True)
  slug            = models.SlugField(_("Post Slug"), unique=True)
  body            = models.TextField(_("Post Content"))
  meta_description = models.CharField(max_length=150, blank=True)
  createdAt       = models.DateTimeField(auto_now_add=True)
  updatedAt       = models.DateTimeField(auto_now=True)
  publishedAt     = models.DateTimeField(blank=True, null=True)
  published       = models.BooleanField(_("Published"), default=False)
  author          = models.ForeignKey("Profile", verbose_name=_(""), on_delete=models.CASCADE)
  tags            = models.ManyToManyField("Tag", verbose_name=_("Tags"), blank=True)
  
  class Meta:
    ordering = ['-publishedAt']
  
  def __str__(self):
    return self.title