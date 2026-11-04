from django.db import models


class Feature(models.Model):
    GROUP_ACTIVITY = 'activity'
    GROUP_ABOUT = 'about'
    GROUP_INTRODUCE = 'introduce'
    GROUP_OPTION = 'option'
    GROUP_CONTENT = 'content'
    GROUP_CHOICES = [
        (GROUP_ACTIVITY, 'فعالیت‌ها'),
        (GROUP_ABOUT, 'ویژگی‌های درباره ما'),
        (GROUP_INTRODUCE, 'باکس‌های معرفی'),
        (GROUP_OPTION, 'خدمات/آپشن‌ها'),
        (GROUP_CONTENT, 'چک‌لیست در دسترس بودن'),
    ]

    group = models.CharField('گروه', max_length=20, choices=GROUP_CHOICES)
    title = models.CharField('عنوان', max_length=200)
    text = models.TextField('متن', blank=True)
    icon = models.CharField(
        'آیکون استاتیک', max_length=100, blank=True,
        help_text='مثل f1.svg یا 1.png یا feature-1.svg (از پوشه static/img)'
    )
    image = models.ImageField('تصویر سفارشی', upload_to='features/',
                              blank=True, null=True)
    order = models.PositiveIntegerField('ترتیب', default=0)

    class Meta:
        ordering = ['group', 'order']
        verbose_name = 'باکس ویژگی'
        verbose_name_plural = 'باکس‌های ویژگی'

    def __str__(self):
        return f'[{self.get_group_display()}] {self.title}'