from django.db import models
from django.conf import settings

# Create your models here.

# CATEGORY_CHOICES = (
#     ("fantasy", "Fantasy"),
#     ("mystery", "Mystery"),
#     ("thriller", "Thriller"),
#     ("historical", "Historical"),
# )

class Listing(models.Model):
    title = models.CharField(max_length=80)
    author = models.CharField(max_length=50)
    description = models.TextField()
    category = models.CharField(max_length=25)#, choices=CATEGORY_CHOICES, default="mystery")
    quantity = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} - {self.author}"
