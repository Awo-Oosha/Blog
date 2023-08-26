from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    image= models.FileField(null=True, upload_to='category/images')

    class Meta:
        verbose_name_plural = "Categories"
        db_table = "Category"

    def __str__(self):
        return (self.name)
    
class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return (self.name)

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True,)
    content = models.TextField()
    myfile = models.FileField(null=True, upload_to='images/post')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='posts')
    tags = models.ManyToManyField(Tag, related_name="posts")
    pub_date = models.DateTimeField(auto_now_add=True)
    post_choices = [
    ('P', 'Publish'),
    ('D', 'Draft'),
    ]
    status = models.CharField(max_length=10, choices= post_choices, default= "D", null=True)
    view_counts = models.IntegerField(default=0,)

    class Meta:
        verbose_name_plural = "Posts"
        db_table = "Post"
        ordering = ["-pub_date"]

    def __str__(self):
        return (self.title)
    

class Comment(models.Model):
    author = models.CharField(max_length=255)
    content =  models.TextField(max_length=500)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f"On {self.post}: {self.author} commented {self.content}"
    