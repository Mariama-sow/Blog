from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Articles(models.Model):
    title = models.CharField(max_length=100)
    sumary = models.CharField(max_length=200)
    date_pub = models.DateTimeField(null=True,default=timezone.now)
    content = models.TextField(default="Contenu par défaut")
    cover = models.ImageField(upload_to='covers/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=False)



    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.TextField(verbose_name='contenu')
    created_at = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Articles, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=False)

    def __str__(self):
        return f"{self.created_at}"