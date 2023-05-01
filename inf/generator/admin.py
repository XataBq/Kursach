from django.contrib import admin
from .models import *
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class Task1AdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Task2
        fields = '__all__'


class Task2AdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Task2
        fields = '__all__'


class Task3AdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Task3
        fields = '__all__'


class Task4AdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Task4
        fields = '__all__'


class Task5AdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Task5
        fields = '__all__'


class Task6AdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Task6
        fields = '__all__'


class Task7AdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Task7
        fields = '__all__'


class Task8AdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Task8
        fields = '__all__'


class Task9AdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Task9
        fields = '__all__'


class Task10AdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Task10
        fields = '__all__'


class Task11AdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Task11
        fields = '__all__'


class Task12AdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Task12
        fields = '__all__'


class Task13AdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Task13
        fields = '__all__'


class Task14AdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Task14
        fields = '__all__'


class Task15AdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Task15
        fields = '__all__'


class Task16AdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Task16
        fields = '__all__'


class Task17AdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Task17
        fields = '__all__'


class Task18AdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Task18
        fields = '__all__'


class Task19AdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Task19
        fields = '__all__'


class Task20AdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Task20
        fields = '__all__'


class Task21AdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Task21
        fields = '__all__'


class Task22AdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Task22
        fields = '__all__'


class Task23AdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Task23
        fields = '__all__'


class Task24AdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Task24
        fields = '__all__'


class Task25AdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Task25
        fields = '__all__'


class Task26AdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Task26
        fields = '__all__'


class Task27AdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Task27
        fields = '__all__'


class VariantAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'task1', 'task2', 'task3', 'task4', 'task5']


class TaskAdmin1(admin.ModelAdmin):
    list_display = ['id', 'content']
    form = Task1AdminForm


class TaskAdmin2(admin.ModelAdmin):
    list_display = ['id', 'content']
    form = Task2AdminForm


class TaskAdmin3(admin.ModelAdmin):
    list_display = ['id', 'content']
    form = Task3AdminForm


class TaskAdmin4(admin.ModelAdmin):
    list_display = ['id', 'content']
    form = Task4AdminForm


class TaskAdmin5(admin.ModelAdmin):
    list_display = ['id', 'content']
    form = Task5AdminForm


class TaskAdmin6(admin.ModelAdmin):
    list_display = ['id', 'content']
    form = Task6AdminForm


class TaskAdmin7(admin.ModelAdmin):
    list_display = ['id', 'content']
    form = Task7AdminForm


class TaskAdmin8(admin.ModelAdmin):
    list_display = ['id', 'content']
    form = Task8AdminForm


class TaskAdmin9(admin.ModelAdmin):
    list_display = ['id', 'content']
    form = Task9AdminForm


class TaskAdmin10(admin.ModelAdmin):
    list_display = ['id', 'content']
    form = Task10AdminForm


class TaskAdmin11(admin.ModelAdmin):
    list_display = ['id', 'content']
    form = Task11AdminForm


class TaskAdmin12(admin.ModelAdmin):
    list_display = ['id', 'content']
    form = Task12AdminForm


class TaskAdmin13(admin.ModelAdmin):
    list_display = ['id', 'content']
    form = Task13AdminForm


class TaskAdmin14(admin.ModelAdmin):
    list_display = ['id', 'content']
    form = Task14AdminForm


class TaskAdmin15(admin.ModelAdmin):
    list_display = ['id', 'content']
    form = Task15AdminForm


class TaskAdmin16(admin.ModelAdmin):
    list_display = ['id', 'content']
    form = Task16AdminForm


class TaskAdmin17(admin.ModelAdmin):
    list_display = ['id', 'content']
    form = Task17AdminForm


class TaskAdmin18(admin.ModelAdmin):
    list_display = ['id', 'content']
    form = Task18AdminForm


class TaskAdmin19(admin.ModelAdmin):
    list_display = ['id', 'content']
    form = Task19AdminForm


class TaskAdmin20(admin.ModelAdmin):
    list_display = ['id', 'content']
    form = Task20AdminForm


class TaskAdmin21(admin.ModelAdmin):
    list_display = ['id', 'content']
    form = Task21AdminForm


class TaskAdmin22(admin.ModelAdmin):
    list_display = ['id', 'content']
    form = Task22AdminForm


class TaskAdmin23(admin.ModelAdmin):
    list_display = ['id', 'content']
    form = Task23AdminForm


class TaskAdmin24(admin.ModelAdmin):
    list_display = ['id', 'content']
    form = Task24AdminForm


class TaskAdmin25(admin.ModelAdmin):
    list_display = ['id', 'content']
    form = Task25AdminForm


class TaskAdmin26(admin.ModelAdmin):
    list_display = ['id', 'content']
    form = Task26AdminForm


class TaskAdmin27(admin.ModelAdmin):
    list_display = ['id', 'content']
    form = Task27AdminForm


admin.site.register(Task1, TaskAdmin1)
admin.site.register(Task2, TaskAdmin2)
admin.site.register(Task3, TaskAdmin3)
admin.site.register(Task4, TaskAdmin4)
admin.site.register(Task5, TaskAdmin5)
admin.site.register(Task6, TaskAdmin6)
admin.site.register(Task7, TaskAdmin7)
admin.site.register(Task8, TaskAdmin8)
admin.site.register(Task9, TaskAdmin9)
admin.site.register(Task10, TaskAdmin10)
admin.site.register(Task11, TaskAdmin11)
admin.site.register(Task12, TaskAdmin12)
admin.site.register(Task13, TaskAdmin13)
admin.site.register(Task14, TaskAdmin14)
admin.site.register(Task15, TaskAdmin15)
admin.site.register(Task16, TaskAdmin16)
admin.site.register(Task17, TaskAdmin17)
admin.site.register(Task18, TaskAdmin18)
admin.site.register(Task19, TaskAdmin19)
admin.site.register(Task20, TaskAdmin20)
admin.site.register(Task21, TaskAdmin21)
admin.site.register(Task22, TaskAdmin22)
admin.site.register(Task23, TaskAdmin23)
admin.site.register(Task24, TaskAdmin24)
admin.site.register(Task25, TaskAdmin25)
admin.site.register(Task26, TaskAdmin26)
admin.site.register(Task27, TaskAdmin27)
admin.site.register(Variant, VariantAdmin)
