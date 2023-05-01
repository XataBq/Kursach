from django import forms


class VarForm(forms.Form):
    variant = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}), required=False,
                                 label='Введите вариант')


class TaskForm(forms.Form):
    task1 = forms.BooleanField(required=False, label="1", initial=True)
    task2 = forms.BooleanField(required=False, label="2", initial=True)
    task3 = forms.BooleanField(required=False, label="3", initial=True)
    task4 = forms.BooleanField(required=False, label="4", initial=True)
    task5 = forms.BooleanField(required=False, label="5", initial=True)
    task6 = forms.BooleanField(required=False, label="6", initial=True)
    task7 = forms.BooleanField(required=False, label="7", initial=True)
    task8 = forms.BooleanField(required=False, label="8", initial=True)
    task9 = forms.BooleanField(required=False, label="9", initial=True)
    task10 = forms.BooleanField(required=False, label="10", initial=True)
    task11 = forms.BooleanField(required=False, label="11", initial=True)
    task12 = forms.BooleanField(required=False, label="12", initial=True)
    task13 = forms.BooleanField(required=False, label="13", initial=True)
    task14 = forms.BooleanField(required=False, label="14", initial=True)
    task15 = forms.BooleanField(required=False, label="15", initial=True)
    task16 = forms.BooleanField(required=False, label="16", initial=True)
    task17 = forms.BooleanField(required=False, label="17", initial=True)
    task18 = forms.BooleanField(required=False, label="18", initial=True)
    task19 = forms.BooleanField(required=False, label="19", initial=True)
    task20 = forms.BooleanField(required=False, label="20", initial=True)
    task21 = forms.BooleanField(required=False, label="21", initial=True)
    task22 = forms.BooleanField(required=False, label="22", initial=True)
    task23 = forms.BooleanField(required=False, label="23", initial=True)
    task24 = forms.BooleanField(required=False, label="24", initial=True)
    task25 = forms.BooleanField(required=False, label="25", initial=True)
    task26 = forms.BooleanField(required=False, label="26", initial=True)
    task27 = forms.BooleanField(required=False, label="27", initial=True)


class AnswerForm(forms.Form):
    answer1 = forms.CharField(required=False)
    answer2 = forms.CharField(required=False)
    answer3 = forms.CharField(required=False)
    answer4 = forms.CharField(required=False)
    answer5 = forms.CharField(required=False)
    answer6 = forms.CharField(required=False)
    answer7 = forms.CharField(required=False)
    answer8 = forms.CharField(required=False)
    answer9 = forms.CharField(required=False)
    answer10 = forms.CharField(required=False)
    answer11 = forms.CharField(required=False)
    answer12 = forms.CharField(required=False)
    answer13 = forms.CharField(required=False)
    answer14 = forms.CharField(required=False)
    answer15 = forms.CharField(required=False)
    answer16 = forms.CharField(required=False)
    answer17 = forms.CharField(required=False)
    answer18 = forms.CharField(required=False)
    answer19 = forms.CharField(required=False)
    answer20 = forms.CharField(required=False)
    answer21 = forms.CharField(required=False)
    answer22 = forms.CharField(required=False)
    answer23 = forms.CharField(required=False)
    answer24 = forms.CharField(required=False)
    answer25 = forms.CharField(required=False)
    answer26 = forms.CharField(required=False)
    answer27 = forms.CharField(required=False)

    widgets = {
        'answer1': forms.TextInput(attrs={'class': 'form-control'}),
        'answer2': forms.TextInput(attrs={'class': 'form-control'}),
        'answer3': forms.TextInput(attrs={'class': 'form-control'}),
        'answer4': forms.TextInput(attrs={'class': 'form-control'}),
        'answer5': forms.TextInput(attrs={'class': 'form-control'}),
        'answer6': forms.TextInput(attrs={'class': 'form-control'}),
        'answer7': forms.TextInput(attrs={'class': 'form-control'}),
        'answer8': forms.TextInput(attrs={'class': 'form-control'}),
        'answer9': forms.TextInput(attrs={'class': 'form-control'}),
        'answer10': forms.TextInput(attrs={'class': 'form-control'}),
        'answer11': forms.TextInput(attrs={'class': 'form-control'}),
        'answer12': forms.TextInput(attrs={'class': 'form-control'}),
        'answer13': forms.TextInput(attrs={'class': 'form-control'}),
        'answer14': forms.TextInput(attrs={'class': 'form-control'}),
        'answer15': forms.TextInput(attrs={'class': 'form-control'}),
        'answer16': forms.TextInput(attrs={'class': 'form-control'}),
        'answer17': forms.TextInput(attrs={'class': 'form-control'}),
        'answer18': forms.TextInput(attrs={'class': 'form-control'}),
        'answer19': forms.TextInput(attrs={'class': 'form-control'}),
        'answer20': forms.TextInput(attrs={'class': 'form-control'}),
        'answer21': forms.TextInput(attrs={'class': 'form-control'}),
        'answer22': forms.TextInput(attrs={'class': 'form-control'}),
        'answer23': forms.TextInput(attrs={'class': 'form-control'}),
        'answer24': forms.TextInput(attrs={'class': 'form-control'}),
        'answer25': forms.TextInput(attrs={'class': 'form-control'}),
        'answer26': forms.TextInput(attrs={'class': 'form-control'}),
        'answer27': forms.TextInput(attrs={'class': 'form-control'}),

    }
