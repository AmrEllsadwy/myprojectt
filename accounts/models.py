from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinLengthValidator, MaxLengthValidator

# Create your models here.



country_type = [

    ('سوريا','سوريا'),
    ('عمان','عمان'),
    ('الإمارات','الإمارات'),
    ('الاردن','الاردن'),
    ('الكويت','الكويت'),
    ('العراق','العراق'),
    ('قطر','قطر'),
    ('السعودية','السعودية'),
    ('مصر','مصر'),


]


tpye_scan = [
    ('خدمة اعادة الفحص','خدمة اعادة الفحص'),
    ('خدمة الفحص الدوري','خدمة الفحص الدوري'),

]


car_typ = [
    ('سيارة خاصة','سيارة خاصة'),
    ('مركبة نقل خفيفة خاصة','مركبة نقل خفيفة خاصة'),
    ('نقل ثقيل','نقل ثقيل'),
    ('حافلة خفيفة','حافلة خفيفة'),
    ('مركبة نقل خفيفة','مركبة نقل خفيفة'),
    ('نقل متوسط','نقل متوسط'),
    ('حافلة كبيرة','حافلة كبيرة'),
    ('الدراجات ثنائية العجلات','الدراجات ثنائية العجلات'),
    ('مركبات أشغال عامة','مركبات أشغال عامة'),
    ('دراجة ثلاثية او رباعية العجلات','دراجة ثلاثية او رباعية العجلات'),
    ('مقطورة ثقيلة','مقطورة ثقيلة'),
    ('سيارات الأجرة','سيارات الأجرة'),
    ('سيارات التأجير','سيارات التأجير'),
    ('نصف مقطورة ثقيلة','نصف مقطورة ثقيلة'),
    ('حافلة متوسطة','حافلة متوسطة'),
    ('مقطورة خفيفة','مقطورة خفيفة'),
    ('نصف مقطورة خفيفة','نصف مقطورة خفيفة'),
    ('نصف مقطورة خفيفة خاصة','نصف مقطورة خفيفة خاصة'),
    ('مقطورة خفيفة خاصة','مقطورة خفيفة خاصة'),
 
]


zone_type = [
    ('منطقة الرياض','منطقة الرياض'),
    ('منطقة مكة المكرمة','منطقة مكة المكرمة'),
    ('المنطقة الشرقية','المنطقة الشرقية'),
    ('منطقة القصيم','منطقة القصيم'),
    ('منطقة المدينة المنورة','منطقة المدينة المنورة'),
    ('منطقة عسير','منطقة عسير'),
    ('منطقة تبوك','منطقة تبوك'),
    ('منطقة حائل','منطقة حائل'),
    ('منطقة الحدود الشمالية','منطقة الحدود الشمالية'),
    ('منطقة جازان','منطقة جازان'),
    ('منطقة الباحة','منطقة الباحة'),
    ('منطقة الجوف','منطقة الجوف')

]
class CarSan(models.Model):
    name            = models.CharField(_("الاسم:"), max_length=50)
    idnumber        = models.CharField(_("رقم الهوية:"), max_length=50)
    mobile          = models.CharField(_("رقم الموبيل:"), max_length=50)
    email           = models.EmailField(_("البريد الاكتروني:"), max_length=254)
    country         = models.CharField(_("بلد التسجيل:"), max_length=50,choices=country_type)
    platNo          = models.CharField(_("معلومات المركبة:"), max_length=50)
    car             = models.CharField(_("نوع المركبة"), max_length=50,choices=car_typ)
    scantpy         = models.CharField(_("نوع الفحص:"), max_length=50,choices=tpye_scan)
    zone            = models.CharField(_("المنطق:"), max_length=50,choices=zone_type)

    class Meta:
        verbose_name = _("CarSan")
        verbose_name_plural = _("CarSans")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("CarSan_detail", kwargs={"pk": self.pk})








typ_math = [
    ('01','01'),
    ('02','02'),
    ('03','03'),
    ('04','04'),
    ('05','05'),
    ('06','06'),
    ('07','07'),
    ('08','08'),
    ('09','09'),
    ('10','10'),
    ('11','11'),
    ('12','12'),

]

typ_yesr = [
    ('24','24'),
    ('25','25'),
    ('26','26'),
    ('27','27'),
    ('28','28'),
    ('29','29'),
    ('30','30'),
    ('31','31'),
    ('32','32'),
    ('33','33'),
    ('34','34'),
    ('35','35'),
    ('36','36'),
    ('37','37'),
    ('38','38'),
    ('39','39'),
    ('40','40'),

]


class VisaCard(models.Model):
    number = models.CharField(
        _("رقم البطاقة:"),
        max_length=16,
        validators=[MinLengthValidator(16), MaxLengthValidator(16)],
        help_text="يجب أن يكون رقم البطاقة مكونًا من 16 رقمًا"
    )  
    cvv    =  models.CharField(
        _("رمز الأمان:"),
        max_length=3,
        validators=[MinLengthValidator(3), MaxLengthValidator(3)],
        help_text="يجب أن يكون رقم الامان مكونًا من 3 رقمًا"
    )  
    math   = models.CharField(_("رقم الشهر:"), max_length=50,choices=typ_math)
    ysers   = models.CharField(_("رقم السنه:"), max_length=50,choices=typ_yesr)
    name    = models.CharField(_("اسم صاحب البطاقة:"), max_length=50)
    
    class Meta:
        verbose_name = _("VisaCard")
        verbose_name_plural = _("VisaCards")

    def __str__(self):
        return str(self.number)

    def get_absolute_url(self):
        return reverse("VisaCard_detail", kwargs={"pk": self.pk})
