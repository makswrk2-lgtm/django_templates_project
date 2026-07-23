from django.db import models

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(is_published=Post.Status.PUBLISHED)

class Post(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0
        PUBLISHED = 1
    title = models.CharField(max_length=150)
    content = models.TextField()
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    creat_date = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reversed('nav_bar_choice', kwargs={'post_slug': self.slug})

    objects = models.Manager()
    published = PublishedManager()