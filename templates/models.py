from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from django.core.validators import FileExtensionValidator

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())
TYPE_CHOICES = sorted((item, item) for item in ('pdf', 'code', 'word'))


class Template(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
    owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)
    pdf = models.FileField(upload_to='templates_pdf',
                           blank=True,
                           validators=[FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx'])])
    word = models.FileField(upload_to='templates_doc',
                           blank=True,
                           validators=[FileExtensionValidator(allowed_extensions=['doc', 'docx'])])
    type = models.CharField(choices=TYPE_CHOICES, default='pdf', max_length=100)

    class Meta:
        ordering = ('created',)