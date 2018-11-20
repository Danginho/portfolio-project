from django.db import models

# Create your models here.

# Add the blog app to settings
class Blog(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to="images")
# Create a migration