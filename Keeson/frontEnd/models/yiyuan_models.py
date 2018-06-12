from django.db import models
# Create your models here.


class PatientBed(models.Model):
    bed_ID = models.IntegerField(verbose_name='床编号')
    device_id = models.CharField(max_length=64, verbose_name='设备号', blank=True, null=True)
    date = models.DateTimeField(verbose_name='时间', blank=True, null=True)

    class Meta:
        db_table = "yiyuan_beds"
        verbose_name_plural = '病床(yiyuan_beds)'

    def __str__(self):
        return str(self.bed_ID)+'床'


class Patient(models.Model):
    bed_number = models.IntegerField(verbose_name='床号')
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

    class Meta:
        db_table = "yiyuan_demographic"
        verbose_name_plural = '病人基本信息(yiyuan_demographic)'
        unique_together = ['bed_number', 'subject_id']

    def __str__(self):
        return str(self.bed_number) + '-' + str(self.subject_id)


class PatientMH(models.Model):
    bed_number = models.IntegerField(verbose_name='床号')
    subject_id = models.IntegerField(verbose_name='病号')
    inquiry_date = models.DateField(verbose_name='问诊时间', blank=True, null=True)
    past_history = models.CharField(max_length=255, verbose_name='既往史', blank=True, null=True)
    personal_history = models.CharField(max_length=255, verbose_name='个人史', blank=True, null=True)
    family_history = models.CharField(max_length=255, verbose_name='家族史', blank=True, null=True)
    in_symptom = models.CharField(max_length=255, verbose_name='现病史（入院病症）', blank=True, null=True)
    out_symptom = models.CharField(max_length=255, verbose_name='现病史（出院病症）', blank=True, null=True)

    class Meta:
        db_table = "yiyuan_med_history"
        verbose_name_plural = '病人病史(yiyuan_med_history)'

    def __str__(self):
        return str(self.bed_number) + '-' + str(self.subject_id)


class PatientTE(models.Model):
    bed_number = models.IntegerField(verbose_name='床号')
    subject_id = models.IntegerField(verbose_name='病号')
    exam_program = models.CharField(max_length=64, verbose_name='每日检查项目', blank=True, null=True)
    result = models.CharField(max_length=255, verbose_name='检查结果', blank=True, null=True)
    date = models.DateField(verbose_name='问诊时间', blank=True, null=True)
    all_result = models.CharField(max_length=255, verbose_name='总问诊结果', blank=True, null=True)

    class Meta:
        db_table = "yiyuan_trial_element"
        verbose_name_plural = '病人每日问诊(yiyuan_trial_element)'

    def __str__(self):
        return str(self.bed_number) + '-' + str(self.subject_id)


class PatientLB(models.Model):
    bed_number = models.IntegerField(verbose_name='床号')
    subject_id = models.IntegerField(verbose_name='病号')
    date = models.DateField(verbose_name='检验时间', blank=True, null=True)
    category = models.CharField(max_length=64, verbose_name='检验分类', blank=True, null=True)
    subcategory = models.CharField(max_length=64, verbose_name='检验子分类', blank=True, null=True)
    exam_program = models.CharField(max_length=64, verbose_name='检验项目', blank=True, null=True)
    result = models.CharField(max_length=255, verbose_name='检验结果', blank=True, null=True)

    class Meta:
        db_table = "yiyuan_laboratory"
        verbose_name_plural = '病人化验放射检验报告(yiyuan_laboratory)'

    def __str__(self):
        return str(self.bed_number) + '-' + str(self.subject_id)


class PatientEX(models.Model):
    bed_number = models.IntegerField(verbose_name='床号')
    subject_id = models.IntegerField(verbose_name='病号')
    dose = models.CharField(max_length=64, verbose_name='每次用药剂量')
    date = models.DateField(verbose_name='给药日期', blank=True, null=True)

    class Meta:
        db_table = "yiyuan_exposure"
        verbose_name_plural = '病人用药记录(yiyuan_exposure)'

    def __str__(self):
        return str(self.bed_number) + '-' + str(self.subject_id)


class PatientPR(models.Model):
    bed_number = models.IntegerField(verbose_name='床号')
    subject_id = models.IntegerField(verbose_name='病号')
    is_operated = models.BooleanField(verbose_name='是否手术')
    category = models.CharField(max_length=64, verbose_name='手术类别', blank=True, null=True)
    date = models.DateField(verbose_name='手术时间', blank=True, null=True)

    class Meta:
        db_table = "yiyuan_operation"
        verbose_name_plural = '病人手术状况(yiyuan_operation)'

    def __str__(self):
        return str(self.bed_number) + '-' + str(self.subject_id)


class PatientPE(models.Model):
    bed_number = models.IntegerField(verbose_name='床号')
    subject_id = models.IntegerField(verbose_name='病号')
    category = models.CharField(max_length=64, verbose_name='体格检查名称')
    result = models.CharField(max_length=255, verbose_name='体格检查结果')
    date = models.DateField(verbose_name='体格检查日期')

    class Meta:
        db_table = "yiyuan_physical_examination"
        verbose_name_plural = '病人体格检验(yiyuan_physical_examination)'

    def __str__(self):
        return str(self.bed_number) + '-' + str(self.subject_id)
