from django.db import models


class Article(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=50, blank=False, default='标题')
    content = models.CharField(max_length=5000, blank=True, default='')
    owner = models.ForeignKey('auth.User', related_name='articles', on_delete=models.CASCADE)

    class Meta:
        ordering = ('created',)