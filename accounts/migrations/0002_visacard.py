# Generated by Django 4.2.16 on 2024-10-06 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VisaCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(max_length=14, verbose_name='رقم الفيزاء:')),
                ('cvv', models.IntegerField(max_length=3, verbose_name='رقم الامان:')),
                ('math', models.CharField(choices=[('01', '01'), ('02', '02'), ('03', '03'), ('04', '04'), ('05', '05'), ('06', '06'), ('07', '07'), ('08', '08'), ('09', '09'), ('10', '10'), ('11', '11'), ('12', '12')], max_length=50, verbose_name='رقم الشهر:')),
                ('ysers', models.CharField(choices=[('24', '24'), ('25', '25'), ('26', '26'), ('27', '27'), ('28', '28'), ('29', '29'), ('30', '30'), ('31', '31'), ('32', '32'), ('33', '33'), ('34', '34'), ('35', '35'), ('36', '36'), ('37', '37'), ('38', '38'), ('39', '39'), ('40', '40')], max_length=50, verbose_name='رقم السنه:')),
                ('name', models.CharField(max_length=50, verbose_name='اسم صاحب البطاقة:')),
            ],
            options={
                'verbose_name': 'VisaCard',
                'verbose_name_plural': 'VisaCards',
            },
        ),
    ]
