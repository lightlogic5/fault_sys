from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class ErrSysType(models.Model):
    type_name = models.CharField(max_length=15, verbose_name='故障类别')

    def __str__(self):
        return self.type_name


class ErrSys(models.Model):
    err_type = models.ForeignKey(ErrSysType, on_delete=models.DO_NOTHING, verbose_name='故障类别', related_name='errsys_e')
    title = models.CharField(max_length=100, verbose_name='标题')
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='作者')
    content = RichTextUploadingField(verbose_name='正文')
    readed_num = models.IntegerField(default=0, verbose_name='阅读数')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    last_updated_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    def __str__(self):
        return "<文章名: %s>" % self.title

    class Meta:
        ordering = ['-created_time']
