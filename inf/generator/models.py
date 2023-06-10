from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField


class Task1(models.Model):
    title = models.CharField(max_length=100, default='Задание 1', blank=True)
    content = RichTextUploadingField(blank=False, verbose_name='Задание')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Фото к заданию')
    answer = models.TextField(verbose_name='Ответ', blank=False)
    file = models.FileField(upload_to='files/%Y/%m/%d', blank=True, verbose_name='Файл к заданию')

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'Задание 1'
        verbose_name_plural = 'Задание 1'


class Task2(models.Model):
    title = models.CharField(max_length=100, default='Задание 2', blank=True)
    content = models.TextField(blank=True, verbose_name='Задание')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Фото к заданию')
    answer = models.TextField(verbose_name='Ответ', blank=True)
    file = models.FileField(upload_to='files/%Y/%m/%d', blank=True, verbose_name='Файл к заданию')

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'Задание 2'
        verbose_name_plural = 'Задание 2'


class Task3(models.Model):
    title = models.CharField(max_length=100, default='Задание 3', blank=True)
    content = models.TextField(blank=True, verbose_name='Задание')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Фото к заданию')
    answer = models.TextField(verbose_name='Ответ', blank=True)
    file = models.FileField(upload_to='files/%Y/%m/%d', blank=True, verbose_name='Файл к заданию')

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'Задание 3'
        verbose_name_plural = 'Задания 3'


class Task4(models.Model):
    title = models.CharField(max_length=100, default='Задание 4', blank=True)
    content = models.TextField(blank=True, verbose_name='Задание')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Фото к заданию')
    answer = models.TextField(verbose_name='Ответ', blank=True)
    file = models.FileField(upload_to='files/%Y/%m/%d', blank=True, verbose_name='Файл к заданию')

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'Задание 4'
        verbose_name_plural = 'Задания 4'


class Task5(models.Model):
    title = models.CharField(max_length=100, default='Задание 5', blank=True)
    content = models.TextField(blank=True, verbose_name='Задание')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Фото к заданию')
    answer = models.TextField(verbose_name='Ответ', blank=True)
    file = models.FileField(upload_to='files/%Y/%m/%d', blank=True, verbose_name='Файл к заданию')

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'Задание 5'
        verbose_name_plural = 'Задания 5'


class Task6(models.Model):
    title = models.CharField(max_length=100, default='Задание 6', blank=True)
    content = models.TextField(blank=True, verbose_name='Задание')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Фото к заданию')
    answer = models.TextField(verbose_name='Ответ', blank=True)
    file = models.FileField(upload_to='files/%Y/%m/%d', blank=True, verbose_name='Файл к заданию')

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'Задание 6'
        verbose_name_plural = 'Задания 6'


class Task7(models.Model):
    title = models.CharField(max_length=100, default='Задание 7', blank=True)
    content = models.TextField(blank=True, verbose_name='Задание')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Фото к заданию')
    answer = models.TextField(verbose_name='Ответ', blank=True)
    file = models.FileField(upload_to='files/%Y/%m/%d', blank=True, verbose_name='Файл к заданию')

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'Задание 7'
        verbose_name_plural = 'Задания 7'


class Task8(models.Model):
    title = models.CharField(max_length=100, default='Задание 8', blank=True)
    content = models.TextField(blank=True, verbose_name='Задание')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Фото к заданию')
    answer = models.TextField(verbose_name='Ответ', blank=True)
    file = models.FileField(upload_to='files/%Y/%m/%d', blank=True, verbose_name='Файл к заданию')

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'Задание 8'
        verbose_name_plural = 'Задания 8'


class Task9(models.Model):
    title = models.CharField(max_length=100, default='Задание 9', blank=True)
    content = models.TextField(blank=True, verbose_name='Задание')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Фото к заданию')
    answer = models.TextField(verbose_name='Ответ', blank=True)
    file = models.FileField(upload_to='files/%Y/%m/%d', blank=True, verbose_name='Файл к заданию')

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'Задание 9'
        verbose_name_plural = 'Задания 9'


class Task10(models.Model):
    title = models.CharField(max_length=100, default='Задание 10', blank=True)
    content = models.TextField(blank=True, verbose_name='Задание')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Фото к заданию')
    answer = models.TextField(verbose_name='Ответ', blank=True)
    file = models.FileField(upload_to='files/%Y/%m/%d', blank=True, verbose_name='Файл к заданию')

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'Задание 10'
        verbose_name_plural = 'Задания 10'


class Task11(models.Model):
    title = models.CharField(max_length=100, default='Задание 11', blank=True)
    content = models.TextField(blank=True, verbose_name='Задание')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Фото к заданию')
    answer = models.TextField(verbose_name='Ответ', blank=True)
    file = models.FileField(upload_to='files/%Y/%m/%d', blank=True, verbose_name='Файл к заданию')

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'Задание 11'
        verbose_name_plural = 'Задания 11'


class Task12(models.Model):
    title = models.CharField(max_length=100, default='Задание 12', blank=True)
    content = models.TextField(blank=True, verbose_name='Задание')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Фото к заданию')
    answer = models.TextField(verbose_name='Ответ', blank=True)
    file = models.FileField(upload_to='files/%Y/%m/%d', blank=True, verbose_name='Файл к заданию')

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'Задание 12'
        verbose_name_plural = 'Задания 12'


class Task13(models.Model):
    title = models.CharField(max_length=100, default='Задание 13', blank=True)
    content = models.TextField(blank=True, verbose_name='Задание')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Фото к заданию')
    answer = models.TextField(verbose_name='Ответ', blank=True)
    file = models.FileField(upload_to='files/%Y/%m/%d', blank=True, verbose_name='Файл к заданию')

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'Задание 13'
        verbose_name_plural = 'Задания 13'


class Task14(models.Model):
    title = models.CharField(max_length=100, default='Задание 14', blank=True)
    content = models.TextField(blank=True, verbose_name='Задание')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Фото к заданию')
    answer = models.TextField(verbose_name='Ответ', blank=True)
    file = models.FileField(upload_to='files/%Y/%m/%d', blank=True, verbose_name='Файл к заданию')

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'Задание 14'
        verbose_name_plural = 'Задания 14'


class Task15(models.Model):
    title = models.CharField(max_length=100, default='Задание 15', blank=True)
    content = models.TextField(blank=True, verbose_name='Задание')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Фото к заданию')
    answer = models.TextField(verbose_name='Ответ', blank=True)
    file = models.FileField(upload_to='files/%Y/%m/%d', blank=True, verbose_name='Файл к заданию')

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'Задание 15'
        verbose_name_plural = 'Задания 15'


class Task16(models.Model):
    title = models.CharField(max_length=100, default='Задание 16', blank=True)
    content = models.TextField(blank=True, verbose_name='Задание')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Фото к заданию')
    answer = models.TextField(verbose_name='Ответ', blank=True)
    file = models.FileField(upload_to='files/%Y/%m/%d', blank=True, verbose_name='Файл к заданию')

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'Задание 16'
        verbose_name_plural = 'Задания 16'


class Task17(models.Model):
    title = models.CharField(max_length=100, default='Задание 17', blank=True)
    content = models.TextField(blank=True, verbose_name='Задание')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Фото к заданию')
    answer = models.TextField(verbose_name='Ответ', blank=True)
    file = models.FileField(upload_to='files/%Y/%m/%d', blank=True, verbose_name='Файл к заданию')

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'Задание 17'
        verbose_name_plural = 'Задания 17'


class Task18(models.Model):
    title = models.CharField(max_length=100, default='Задание 18', blank=True)
    content = models.TextField(blank=True, verbose_name='Задание')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Фото к заданию')
    answer = models.TextField(verbose_name='Ответ', blank=True)
    file = models.FileField(upload_to='files/%Y/%m/%d', blank=True, verbose_name='Файл к заданию')

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'Задание 18'
        verbose_name_plural = 'Задания 18'


class Task19(models.Model):
    title = models.CharField(max_length=100, default='Задание 19', blank=True)
    content = models.TextField(blank=True, verbose_name='Задание')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Фото к заданию')
    answer = models.TextField(verbose_name='Ответ', blank=True)
    file = models.FileField(upload_to='files/%Y/%m/%d', blank=True, verbose_name='Файл к заданию')

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'Задание 19'
        verbose_name_plural = 'Задания 19'


class Task20(models.Model):
    title = models.CharField(max_length=100, default='Задание 20', blank=True)
    content = models.TextField(blank=True, verbose_name='Задание')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Фото к заданию')
    answer = models.TextField(verbose_name='Ответ', blank=True)
    file = models.FileField(upload_to='files/%Y/%m/%d', blank=True, verbose_name='Файл к заданию')

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'Задание 20'
        verbose_name_plural = 'Задания 20'


class Task21(models.Model):
    title = models.CharField(max_length=100, default='Задание 21', blank=True)
    content = models.TextField(blank=True, verbose_name='Задание')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Фото к заданию')
    answer = models.TextField(verbose_name='Ответ', blank=True)
    file = models.FileField(upload_to='files/%Y/%m/%d', blank=True, verbose_name='Файл к заданию')

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'Задание 21'
        verbose_name_plural = 'Задания 21'


class Task22(models.Model):
    title = models.CharField(max_length=100, default='Задание 22', blank=True)
    content = models.TextField(blank=True, verbose_name='Задание')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Фото к заданию')
    answer = models.TextField(verbose_name='Ответ', blank=True)
    file = models.FileField(upload_to='files/%Y/%m/%d', blank=True, verbose_name='Файл к заданию')

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'Задание 22'
        verbose_name_plural = 'Задания 22'


class Task23(models.Model):
    title = models.CharField(max_length=100, default='Задание 23', blank=True)
    content = models.TextField(blank=True, verbose_name='Задание')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Фото к заданию')
    answer = models.TextField(verbose_name='Ответ', blank=True)
    file = models.FileField(upload_to='files/%Y/%m/%d', blank=True, verbose_name='Файл к заданию')

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'Задание 23'
        verbose_name_plural = 'Задания 23'


class Task24(models.Model):
    title = models.CharField(max_length=100, default='Задание 24', blank=True)
    content = models.TextField(blank=True, verbose_name='Задание')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Фото к заданию')
    answer = models.TextField(verbose_name='Ответ', blank=True)
    file = models.FileField(upload_to='files/%Y/%m/%d', blank=True, verbose_name='Файл к заданию')

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'Задание 24'
        verbose_name_plural = 'Задания 24'


class Task25(models.Model):
    title = models.CharField(max_length=100, default='Задание 25', blank=True)
    content = models.TextField(blank=True, verbose_name='Задание')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Фото к заданию')
    answer = models.TextField(verbose_name='Ответ', blank=True)
    file = models.FileField(upload_to='files/%Y/%m/%d', blank=True, verbose_name='Файл к заданию')

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'Задание 25'
        verbose_name_plural = 'Задания 25'


class Task26(models.Model):
    title = models.CharField(max_length=100, default='Задание 26', blank=True)
    content = models.TextField(blank=True, verbose_name='Задание')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Фото к заданию')
    answer = models.TextField(verbose_name='Ответ', blank=True)
    file = models.FileField(upload_to='files/%Y/%m/%d', blank=True, verbose_name='Файл к заданию')

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'Задание 26'
        verbose_name_plural = 'Задания 26'


class Task27(models.Model):
    title = models.CharField(max_length=100, default='Задание 27', blank=True)
    content = models.TextField(blank=True, verbose_name='Задание')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Фото к заданию')
    answer = models.TextField(verbose_name='Ответ', blank=True)
    file = models.FileField(upload_to='files/%Y/%m/%d', blank=True, verbose_name='Файл к заданию')

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'Задание 27'
        verbose_name_plural = 'Задания 27'


class Variant(models.Model):
    title = models.CharField(max_length=100, blank=True)
    task1 = models.ForeignKey(Task1, on_delete=models.PROTECT)
    task2 = models.ForeignKey(Task2, on_delete=models.PROTECT)
    task3 = models.ForeignKey(Task3, on_delete=models.PROTECT)
    task4 = models.ForeignKey(Task4, on_delete=models.PROTECT)
    task5 = models.ForeignKey(Task5, on_delete=models.PROTECT)
    task6 = models.ForeignKey(Task6, on_delete=models.PROTECT)
    task7 = models.ForeignKey(Task7, on_delete=models.PROTECT)
    task8 = models.ForeignKey(Task8, on_delete=models.PROTECT)
    task9 = models.ForeignKey(Task9, on_delete=models.PROTECT)
    task10 = models.ForeignKey(Task10, on_delete=models.PROTECT)
    task11 = models.ForeignKey(Task11, on_delete=models.PROTECT)
    task12 = models.ForeignKey(Task12, on_delete=models.PROTECT)
    task13 = models.ForeignKey(Task13, on_delete=models.PROTECT)
    task14 = models.ForeignKey(Task14, on_delete=models.PROTECT)
    task15 = models.ForeignKey(Task15, on_delete=models.PROTECT)
    task16 = models.ForeignKey(Task16, on_delete=models.PROTECT)
    task17 = models.ForeignKey(Task17, on_delete=models.PROTECT)
    task18 = models.ForeignKey(Task18, on_delete=models.PROTECT)
    task19 = models.ForeignKey(Task19, on_delete=models.PROTECT)
    task20 = models.ForeignKey(Task20, on_delete=models.PROTECT)
    task21 = models.ForeignKey(Task21, on_delete=models.PROTECT)
    task22 = models.ForeignKey(Task22, on_delete=models.PROTECT)
    task23 = models.ForeignKey(Task23, on_delete=models.PROTECT)
    task24 = models.ForeignKey(Task24, on_delete=models.PROTECT)
    task25 = models.ForeignKey(Task25, on_delete=models.PROTECT)
    task26 = models.ForeignKey(Task26, on_delete=models.PROTECT)
    task27 = models.ForeignKey(Task27, on_delete=models.PROTECT)

    def get_absolute_url(self):
        return reverse('ready_var', kwargs={'pk': self.pk, 'select': '7ffffff'})

    def get_answers(self):
        answers = dict()
        answers['1'] = Task1.objects.get(pk=self.task1.pk).answer
        answers['2'] = Task2.objects.get(pk=self.task2.pk).answer
        answers['3'] = Task3.objects.get(pk=self.task3.pk).answer
        answers['4'] = Task4.objects.get(pk=self.task4.pk).answer
        answers['5'] = Task5.objects.get(pk=self.task5.pk).answer
        answers['6'] = Task6.objects.get(pk=self.task6.pk).answer
        answers['7'] = Task7.objects.get(pk=self.task7.pk).answer
        answers['8'] = Task8.objects.get(pk=self.task8.pk).answer
        answers['9'] = Task9.objects.get(pk=self.task9.pk).answer
        answers['10'] = Task10.objects.get(pk=self.task10.pk).answer
        answers['11'] = Task11.objects.get(pk=self.task11.pk).answer
        answers['12'] = Task12.objects.get(pk=self.task12.pk).answer
        answers['13'] = Task13.objects.get(pk=self.task13.pk).answer
        answers['14'] = Task14.objects.get(pk=self.task14.pk).answer
        answers['15'] = Task15.objects.get(pk=self.task15.pk).answer
        answers['16'] = Task16.objects.get(pk=self.task16.pk).answer
        answers['17'] = Task17.objects.get(pk=self.task17.pk).answer
        answers['18'] = Task18.objects.get(pk=self.task18.pk).answer
        answers['19'] = Task19.objects.get(pk=self.task19.pk).answer
        answers['20'] = Task20.objects.get(pk=self.task20.pk).answer
        answers['21'] = Task21.objects.get(pk=self.task21.pk).answer
        answers['22'] = Task22.objects.get(pk=self.task22.pk).answer
        answers['23'] = Task23.objects.get(pk=self.task23.pk).answer
        answers['24'] = Task24.objects.get(pk=self.task24.pk).answer
        answers['25'] = Task25.objects.get(pk=self.task25.pk).answer
        answers['26'] = Task26.objects.get(pk=self.task26.pk).answer
        answers['27'] = Task27.objects.get(pk=self.task27.pk).answer
        return answers

    class Meta:
        verbose_name = 'Вариант'
        verbose_name_plural = 'Варианты'


all_models = ['', Task1, Task2, Task3, Task4, Task5, Task6, Task7, Task8, Task9, Task10, Task11, Task12, Task13, Task14,
              Task15, Task16, Task17, Task18, Task19, Task20, Task21, Task22, Task23, Task24, Task25, Task26, Task27]
