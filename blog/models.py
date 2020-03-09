from django.db import models
from django.utils import timezone
# Create your models here.
class Post(models.Model):
        CATEGORY_CHOICES =(
            ('Lifestyle', 'Lifestyle'),
            ('Health', 'Health'),
            ('Family', 'Family'),
            ('Technology', 'Technology'),
            ('Travel', 'Travel'),
            ('Work', 'Work'),
        )
        cover = models.FileField(default='')
        title = models.CharField(max_length=2000,default='')
        category = models.CharField(max_length=2000, choices = CATEGORY_CHOICES,default='')
        created_date = models.DateTimeField(default='')
        content = models.TextField(default='')
        # slug = models.SlugField(default='')
        
        class Meta:
            ordering = ['-created_date']

        def __str__(self):
            return self.title