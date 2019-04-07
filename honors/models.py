from django.db import models
TYPE_CHOICES = sorted((item, item) for item in ('ICPC', 'CCPC', '天梯赛', '浙大赛', '浙江省赛', '大事件', '其他'))


class Honor(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=20)
    detail = models.CharField(max_length=500)
    type = models.CharField(choices=TYPE_CHOICES, max_length=10)
    time = models.DateField()

