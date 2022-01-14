from django.db import models

# Create your models here.
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.utils.translation import gettext as _


class Post(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(_("desc"))
    image = models.ImageField(_("image"), upload_to='images')
    slug = models.SlugField(_("slug") , blank=True , null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    """Model definition for Post."""

    # TODO: Define fields here

    class Meta:
        """Meta definition for Post."""

        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        """Unicode representation of Post."""
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Post , self).save(*args, **kwargs)
