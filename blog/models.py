from django.db import models
from django.urls import reverse

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
    category = models.ForeignKey('Category', on_delete=models.PROTECT, related_name = 'posts')

    class Meta:
        ordering = ['creat_date']


    def __str__(self):
        return self.title


    def get_post_url(self):
        return reverse('post', kwargs={'cat_slug': self.category.slug, 'post_slug': self.slug})


    objects = models.Manager()
    published = PublishedManager()


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def get_cat_url(self):
        return reverse('cat', kwargs={'cat_slug': self.slug})


    def __str__(self):
        return self.name