
from django.contrib.auth import get_user_model
from mptt.models import MPTTModel


from django.db import models
from tinymce.models import HTMLField

class Blog(models.Model):
    title = models.CharField(max_length=200)
    main_image = models.ImageField(upload_to='blogs/')
    description = HTMLField()  # TinyMCE-enabled field
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag')
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title



class Category(MPTTModel):
    title = models.CharField(max_length=200)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)

    class MPTTMeta:
        order_insertion_by = ['title']

    def __str__(self):
        return self.title

class Tag(models.Model):
    title = models.CharField(max_length=50)

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    content = models.TextField()
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)

class Menu(models.Model):
    title = models.CharField(max_length=100)
    position = models.PositiveIntegerField()
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    url = models.URLField(null=True, blank=True)
