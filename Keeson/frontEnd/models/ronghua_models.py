from django.db import models
# Create your models here.


# class RonghuaBed(models.Model):
#     bed_ID = models.IntegerField(primary_key=True, verbose_name='床号')
#
#     class Meta:
#         db_table = "ronghua_bed"
#         verbose_name_plural = '荣华病床(ronghua_bed)'
#
#     def __str__(self):
#         return str(self.pk)+'号床'


class DM_Ronghua(models.Model):
    bed_number = models.CharField(max_length=64, verbose_name='床号')
    Gender_Choices = {
        ('M', '男性'),
        ('F', '女性'),
    }
    subject_id = models.IntegerField(verbose_name='病号')
    gender = models.CharField(max_length=64, choices=Gender_Choices, verbose_name='性别', blank=True, null=True)
    age = models.IntegerField(verbose_name='年龄', blank=True, null=True)
    height = models.IntegerField(verbose_name='身高', help_text='(cm)', blank=True, null=True)
    weight = models.FloatField(verbose_name='体重', help_text='(kg)', blank=True, null=True)
    in_date = models.DateTimeField(verbose_name='入院日期', blank=True, null=True)
    out_date = models.DateTimeField(verbose_name='出院日期', blank=True, null=True)
    in_diagnose = models.CharField(max_length=255, verbose_name='入院诊断', blank=True, null=True)

    class Meta:
        db_table = "ronghua_demographic"
        verbose_name_plural = '荣华客户基本信息(ronghua_demographic)'
        unique_together = ['bed_number', 'subject_id']

    def __str__(self):
        return str(self.bed_number) + '-' + str(self.subject_id)


class EX_Ronghua(models.Model):
    bed_number = models.CharField(max_length=64, verbose_name='床号')
    subject_id = models.IntegerField(verbose_name='病号')
    dose = models.CharField(max_length=64, verbose_name='每次用药剂量', blank=True, null=True)
    unit = models.CharField(max_length=64, verbose_name='剂量单位', blank=True, null=True)
    doctor_advice = models.CharField(max_length=255, verbose_name='医嘱类型', blank=True, null=True)
    date = models.DateField(verbose_name='给药日期', blank=True, null=True)

    class Meta:
        db_table = "ronghua_exposure"
        verbose_name_plural = '荣华用药记录(ronghua_exposure)'

    def __str__(self):
        return str(self.bed_number) + '-' + str(self.subject_id)


class NU_Ronghua(models.Model):
    bed_number = models.CharField(max_length=64, verbose_name='床号')
    subject_id = models.IntegerField(verbose_name='病号')
    category = models.CharField(max_length=64, verbose_name='护理分类', blank=True, null=True)
    result = models.CharField(max_length=255, verbose_name='护理结果', blank=True, null=True)
    date = models.DateField(verbose_name='护理时间', blank=True, null=True)

    class Meta:
        db_table = "ronghua_nursing"
        verbose_name_plural = '荣华护理记录(ronghua_nursing)'

    def __str__(self):
        return str(self.bed_number) + '-' + str(self.subject_id)


class PE_Ronghua(models.Model):
    bed_number = models.CharField(max_length=64, verbose_name='床号')
    subject_id = models.IntegerField(verbose_name='病号')
    is_operated = models.BooleanField(verbose_name='是否手术')
    category = models.CharField(max_length=64, verbose_name='检验分类', blank=True, null=True)
    result = models.CharField(max_length=255, verbose_name='检验结果', blank=True, null=True)
    date = models.DateField(verbose_name='检验时间', blank=True, null=True)

    class Meta:
        db_table = "ronghua_physical_examination"
        verbose_name_plural = '荣华体检表(ronghua_physical_examination)'

    def __str__(self):
        return str(self.bed_number) + '-' + str(self.subject_id)


class BB_Ronghua(models.Model):
    bed_number = models.CharField(max_length=64, verbose_name='床号')
    subject_id = models.IntegerField(verbose_name='病号')
    category = models.CharField(max_length=64, verbose_name='检验分类', blank=True, null=True)
    result = models.CharField(max_length=255, verbose_name='检验结果', blank=True, null=True)
    date = models.DateField(verbose_name='检验时间', blank=True, null=True)

    class Meta:
        db_table = "ronghua_baby"
        verbose_name_plural = '荣华婴儿表(ronghua_baby)'

    def __str__(self):
        return str(self.bed_number) + '-' + str(self.subject_id)
