from django.core.management.base import BaseCommand

from core.models import (SiteSettings, IntroMessage, HeroSection,
                         AboutSection, ContentBlock)
from services.models import Feature
from projects.models import Project


class Command(BaseCommand):
    help = 'ایجاد داده‌های نمونه مطابق طرح اولیه'

    def handle(self, *args, **opts):
        # سینگلتون‌ها
        SiteSettings.load()
        IntroMessage.load()
        HeroSection.load()
        AboutSection.load()
        ContentBlock.load()

        # فعالیت‌ها
        activities = [
            ('برنامه ریزی و هدف گذاری', 'برای بهبود اوضاع کسب و کار شما و تحقق اهدافتون برنامه داریم.', 'f1.svg'),
            ('پشتیبانی اختصاصی',
             'از زمان شروع همکاری تا همیشه در کنار شما هستیم و مشکلات و سوالات شما رو برطرف میکنیم.', 'f2.svg'),
            ('ایده های خلاقانه و بی نظیر', 'تیم ما به شما کمک میکنه ایده های خودتون رو به واقعیت تبدیل کنید.',
             'f4.svg'),
            ('طراحی زیبا و مدرن', 'یک طراحی زیبا و منحصربفرد به شما کمک میکنه که بهتر دیده بشید!', 'f3.svg'),
        ]
        for i, (t, txt, icon) in enumerate(activities):
            Feature.objects.get_or_create(
                group=Feature.GROUP_ACTIVITY, title=t,
                defaults={'text': txt, 'icon': icon, 'order': i}
            )

        about = [
            ('همیشه پاسخگو', 'feature-1.svg'),
            ('طراحی مدرن و تمیز', 'feature-2.svg'),
            ('تست روی چند دستگاه', 'feature-3.svg'),
            ('تجربه کاربری عالی', 'feature-4.svg'),
        ]
        for i, (t, icon) in enumerate(about):
            Feature.objects.get_or_create(
                group=Feature.GROUP_ABOUT, title=t,
                defaults={'icon': icon, 'order': i}
            )

        introduce = [
            ('سریع و با کیفیت', 'در سریع ترین زمان ممکن و با بالاترین کیفیت پروژه خود را تحویل بگیرید.', 'f1 (1).svg'),
            ('مشاوره و راهنمایی', 'تجربیات و دانش خود را در زمینه ی بازاریابی در اختیار شما قرار میدهیم', 'f4 (1).svg'),
            ('بدون محدودیت زمانی و مکانی', 'در هر زمان و در هرمکان میتوانید از خدمات تیم ما استفاده کنید.',
             'f2 (1).svg'),
            ('توجه به درخواست شما', 'تمامی درخواست شما را به دقت بررسی کرده و در پروژه ی شما پیاده میکنیم.', 'f5.svg'),
            ('پشتیبانی نامحدود', 'از آغاز تا پایان در کنار شما پاسخگوی سوالات و مشکلات شما هستیم.', 'f3 (1).svg'),
            ('سریع و با کیفیت', 'در سریع ترین زمان ممکن و با بالاترین کیفیت پروژه خود را تحویل بگیرید.', 'f6.svg'),
        ]
        for i, (t, txt, icon) in enumerate(introduce):
            Feature.objects.get_or_create(
                group=Feature.GROUP_INTRODUCE, title=t,
                defaults={'text': txt, 'icon': icon, 'order': i}
            )

        options = [
            ('مشاوره و راهنمایی', '1.png'),
            ('بررسی نیاز و پیش بینی نیاز بازار', '2.png'),
            ('بررسی نقاط قوت و ضعف شما', '3.png'),
        ]
        for i, (t, icon) in enumerate(options):
            Feature.objects.get_or_create(
                group=Feature.GROUP_OPTION, title=t,
                defaults={'icon': icon, 'order': i}
            )

        content = [
            ('انجام خدمات سئو',
             'سئو به شما کمک میکنید در نتایج جستجوی گوگل رتبه بهتری کسب کنید و فروش بیشتری داشته باشید.'),
            ('انجام پروژه های بزرگ تجاری',
             'ما برای افرادی که قصد راه اندازی ایده های تجاری و بزرگ دارند نیز برنامه داریم، تخصص ما مبارزه با محدودیت هاست.'),
        ]
        for i, (t, txt) in enumerate(content):
            Feature.objects.get_or_create(
                group=Feature.GROUP_CONTENT, title=t,
                defaults={'text': txt, 'order': i}
            )

        projects = [
            ('هوشانه', 'فروشگاه', 'https://example.com/hooshaneh'),
            ('باشگاه یار', 'اپلیکیشن مدیریت باشگاه', 'https://example.com/bashgah-yar'),
            ('فرخ رخ', 'فروشگاه', 'https://example.com/farokh-rokh'),
            ('آژا فیت', 'وبلاگ ورزشی', 'https://example.com/azha-fit'),
            ('لینکدونی', 'اپلیکیشن', 'https://example.com/linkdoni'),
            ('فات چمپیون', 'فروشگاه', 'https://example.com/fat-champion'),
        ]
        for i, (t, cat, link) in enumerate(projects):
            Project.objects.update_or_create(
                title=t,
                defaults={'category': cat, 'order': i, 'link': link},
            )

        self.stdout.write(self.style.SUCCESS('داده‌های نمونه با موفقیت ایجاد شد.'))
