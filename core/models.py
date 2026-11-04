from django.db import models


class SingletonModel(models.Model):
    """مدل تک‌نمونه‌ای که همیشه pk=1 دارد."""
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class SiteSettings(SingletonModel):
    site_name = models.CharField('نام سایت', max_length=100, default='فراکد')
    site_title = models.CharField('عنوان مرورگر', max_length=200,
                                  default='faracode team | تیم فراکد')
    logo = models.ImageField('لوگو', upload_to='site/', blank=True, null=True)
    favicon = models.ImageField('فاوآیکون', upload_to='site/', blank=True, null=True)
    preloader = models.ImageField('لودیگ', upload_to='site/', blank=True, null=True)
    email = models.EmailField('ایمیل', default='faracodeteam@gmail.com')
    phone = models.CharField('تلفن', max_length=50, default='09123242423')
    address = models.CharField('آدرس', max_length=255, default='اهواز، کیان آباد')
    instagram_url = models.URLField('اینستاگرام', blank=True,
                                    default='https://instagram.com/faracodeteam')
    telegram_url = models.URLField('تلگرام', blank=True,
                                   default='https://t.me/Samancfu')
    whatsapp_url = models.URLField('واتساپ', blank=True,
                                   default='https://wa.me/+989910549803')

    class Meta:
        verbose_name = 'تنظیمات سایت'
        verbose_name_plural = 'تنظیمات سایت'

    def __str__(self):
        return self.site_name


class IntroMessage(SingletonModel):
    line1 = models.CharField('خط اول', max_length=100, default='به وبسایت ما')
    line2 = models.CharField('خط دوم', max_length=100, default='خوش اومدین')

    class Meta:
        verbose_name = 'پیام خوش‌آمد'
        verbose_name_plural = 'پیام خوش‌آمد'


class HeroSection(SingletonModel):
    badge = models.CharField('برچسب', max_length=200,
                             default='بگذار کدها به جای تو کار کنند')
    title = models.CharField('عنوان', max_length=200,
                             default='گروه برنامه نویسی فراکد')
    description = models.TextField('توضیح', default=(
        'گروه برنامه نویسی فراکد متشکل از برنامه نویسان مجرب و متعهد آماده ی '
        'پیاده سازی و ساخت انواع اپلیکیشن ها و وبسایت های شرکتی و فروشگاهی با '
        'بالاترین کیفیت و مناسب ترین قیمت.'
    ))
    image = models.ImageField('تصویر', upload_to='hero/', blank=True, null=True)
    primary_btn_text = models.CharField(max_length=50, default='تماس با ما')
    primary_btn_url = models.CharField(max_length=200, default='#conect')
    secondary_btn_text = models.CharField(max_length=50, default='بیشتر بخون')
    secondary_btn_url = models.CharField(max_length=200, default='#optionss')

    class Meta:
        verbose_name = 'هدر اصلی (Hero)'
        verbose_name_plural = 'هدر اصلی (Hero)'


class AboutSection(SingletonModel):
    badge = models.CharField(max_length=200, default='مسئولیت پذیری و وقت شناسی')
    title = models.CharField(max_length=200,
                             default='وبسایت و اپلیکیشن شمارو خاص جلوه میده!')
    description = models.TextField(default=(
        'امروزه بیشتر افراد ترجیح میدن بجای تحمل ترافیک و اتلاف کردن زمان، '
        'در منزل راحت بشینن و به خرید بپردازن! مردم اولین جایی که به دنبال '
        'خدمات شما می گردن، در اینترنت هست! ...'
    ))
    image = models.ImageField(upload_to='about/', blank=True, null=True)

    class Meta:
        verbose_name = 'بخش درباره ما'
        verbose_name_plural = 'بخش درباره ما'


class ContentBlock(SingletonModel):
    """بخش «ما کمک می کنیم همیشه در دسترس باشید»"""
    badge = models.CharField(max_length=200, default='محدودیت زمانی را از بین ببرید!')
    title = models.CharField(max_length=200,
                             default='ما کمک می کنیم همیشه در دسترس باشید!')
    description = models.TextField(default=(
        'با داشتن وب سایت در 24 ساعت شبانه‌روز، 7روز هفته در کنار مشتری هستید...'
    ))
    video = models.FileField(upload_to='videos/', blank=True, null=True)
    video_thumbnail = models.ImageField(upload_to='content/', blank=True, null=True)

    class Meta:
        verbose_name = 'بخش «در دسترس بودن»'
        verbose_name_plural = 'بخش «در دسترس بودن»'