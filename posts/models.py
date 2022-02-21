from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Post(models.Model):
    title = models.CharField(verbose_name="Title", max_length=120)
    content = models.CharField(verbose_name="Content", max_length=528)
    creation_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, verbose_name="Author", on_delete=models.CASCADE)

    @property
    def upvotes(self):
        return Upvote.objects.filter(post=self).count()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("id",)


class Upvote(models.Model):
    post = models.ForeignKey(Post, verbose_name="upvotes", on_delete=models.CASCADE)
    author = models.ForeignKey(User, verbose_name="upvotes", on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("id",)
