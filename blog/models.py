import uuid
from random import choices
from django.db import models
from django.urls import reverse
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    title = models.CharField(('title'), max_length=200)
    text = models.TextField()
    tags = models.CharField('tags', max_length = 100)
    pub_date = models.DateTimeField(default = timezone.now)
    created_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.pub_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"id": self.id})
    
class PostType(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4)
    Post = models.ForeignKey('Post', on_delete=models.SET_NULL, null = True)
    POST_CATEGORY = (
        ('tech', 'Technology'),
        ('article', 'article'),
        ('fic', 'Fiction'),
        ('non', 'Non-Fiction'),
        ('py', 'Python'),
        ('dj', 'Django'),
        ('Web', 'Web Development'),
        ('js', 'Javascript'),
        ('frontend', 'Frontend Development'),
        ('backend', 'Backend Development'),
    )

    Tag = models.CharField(
        max_length = 10,
        choices = POST_CATEGORY,
        blank = True,
        default = 'article'
    )

class meta:
        ordering = ['POST_CATEGORY']

def __str__(self):
        return f'{self.id} ({self.post.title})'

class Author(models.Model):
    First_Name = models.CharField(max_length = 100)
    Last_Name = models.CharField(max_length = 100)
    Position = models.CharField(max_length = 100)

class meta:
    ordering = ['First_Name', 'Last_Name']

def get_absolute_url(self):
    return reverse('author_detail', args=[str(self.id)])

def __str__(self):
    return f'{self.Last_Name}, {self.First_Name}'