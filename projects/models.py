from django.db import models
from django.utils.text import slugify


class Project(models.Model):
    title = models.CharField('عنوان', max_length=200)
    category = models.CharField('دسته‌بندی', max_length=100)
    image = models.ImageField('تصویر', upload_to='projects/',
                              blank=True, null=True)
    slug = models.SlugField('نامک', unique=True, blank=True)
    order = models.PositiveIntegerField('ترتیب', default=0)
    is_active = models.BooleanField('فعال', default=True)

    # ⬇⬇⬇ دو فیلد جدید ⬇⬇⬇
    link = models.URLField(
        'لینک پروژه', blank=True,
        help_text='لینکی که با کلیک روی عنوان پروژه باز می‌شود (مثلاً https://example.com)'
    )
    open_in_new_tab = models.BooleanField(
        'باز شدن در تب جدید', default=True,
        help_text='اگر تیک داشته باشد، لینک در تب جدید مرورگر باز می‌شود.'
    )
    # ⬆⬆⬆ پایان دو فیلد جدید ⬆⬆⬆

    class Meta:
        ordering = ['order']
        verbose_name = 'پروژه'
        verbose_name_plural = 'پروژه‌ها'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title