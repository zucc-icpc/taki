from django.db import models
TYPE_CHOICES = sorted((item, item) for item in ('ICPC', 'CCPC', '天梯赛', '浙大赛', '浙江省赛', '大事件', '其他'))


class Honor(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=20, default="")
    intro = models.CharField(max_length=200, default="")
    detail = models.CharField(max_length=5000, default="")
    type = models.CharField(choices=TYPE_CHOICES, max_length=10)
    time = models.DateField()

    class Meta:
        ordering = ('-time',)

