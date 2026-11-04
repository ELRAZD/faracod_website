from django.db import models


class ContactMessage(models.Model):
    KIND_CONTACT = 'contact'
    KIND_PROJECT = 'project'
    KIND_CHOICES = [
        (KIND_CONTACT, 'پیام تماس'),
        (KIND_PROJECT, 'درخواست پروژه'),
    ]

    kind = models.CharField('نوع', max_length=20, choices=KIND_CHOICES,
                            default=KIND_CONTACT)
    name = models.CharField('نام', max_length=100)
    email = models.EmailField('ایمیل')
    subject = models.CharField('موضوع', max_length=200, blank=True)
    message = models.TextField('پیام')
    created_at = models.DateTimeField('تاریخ ثبت', auto_now_add=True)
    is_read = models.BooleanField('خوانده شده', default=False)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'پیام'
        verbose_name_plural = 'پیام‌ها'

    def __str__(self):
        return f'{self.get_kind_display()} — {self.name}'