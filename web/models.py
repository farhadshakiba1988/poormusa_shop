from datetime import datetime
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.FileField(upload_to='files/user_avatar', null=True, blank=True)
    description = models.CharField(max_length=512, null=False, blank=False)


class Category(models.Model):
    title = models.CharField(max_length=128, null=False, blank=False)
    cover = models.FileField(upload_to='files/category_cover/', null=False, blank=False)

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=128, null=False, blank=False)
    cover = models.FileField(upload_to='files/article_cover/', null=False, blank=False)
    content = RichTextUploadingField(null=True, blank=True)
    created_at = models.DateTimeField(default=datetime.now, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

