from django.db import models
from django.utils.translation import gettext as _
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.

class Tag(models.Model):
  name    = models.CharField(_("Tag Name"), max_length=50, unique=True)
  
  def __str__(self):
    return self.name  


class Post(models.Model):
  title           = models.CharField(_("Title"), max_length=50, unique=True)
  slug            = models.SlugField(_("Post Slug"), unique=True)
  body            = models.TextField(_("Post Content"))
  createdAt       = models.DateTimeField(auto_now_add=True)
  updatedAt       = models.DateTimeField(auto_now=True)
  published       = models.BooleanField(_("Published"), default=False)
  author          = models.ForeignKey(User, verbose_name=_("Author"), on_delete=models.CASCADE)
  tags            = models.ManyToManyField("Tag", verbose_name=_("Tags"), blank=True)

  class Meta:
    ordering = ['-createdAt']
  
  def __str__(self):
    return self.title