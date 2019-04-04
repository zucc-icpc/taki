from django.db import models


class Solution(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=50, blank=False, default='标题')
    oj = models.CharField(max_length=50, blank=False, default='')
    pid = models.CharField(max_length=50, blank=False, default='')
    content = models.TextField()
    owner = models.ForeignKey('auth.User', related_name='solutions', on_delete=models.CASCADE)

    class Meta:
        ordering = ('created',)