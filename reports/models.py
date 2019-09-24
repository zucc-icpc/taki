from django.db import models


class Report(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=50, blank=False, default='标题')
    content = models.TextField()
    owner = models.ForeignKey('auth.User', related_name='reports', on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created',)