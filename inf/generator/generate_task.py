from random2 import randint
from django.db.models import Max, Min
from .models import *


def random_task(task):
    min_id1 = task.objects.all().aggregate(min_id=Min('id'))['min_id']
    max_id1 = task.objects.all().aggregate(max_id=Max('id'))['max_id']
    while True:
        pk = randint(min_id1, max_id1)
        new_task = task.objects.filter(pk=pk).first()
        if new_task:
            return new_task


def new_variant():
    task1 = random_task(Task1)
    task2 = random_task(Task2)
    task3 = random_task(Task3)
    task4 = random_task(Task4)
    task5 = random_task(Task5)
    task6 = random_task(Task6)
    task7 = random_task(Task7)
    task8 = random_task(Task8)
    task9 = random_task(Task9)
    task10 = random_task(Task10)
    task11 = random_task(Task11)
    task12 = random_task(Task12)
    task13 = random_task(Task13)
    task14 = random_task(Task14)
    task15 = random_task(Task15)
    task16 = random_task(Task16)
    task17 = random_task(Task17)
    task18 = random_task(Task18)
    task19 = random_task(Task19)
    task20 = random_task(Task20)
    task21 = random_task(Task21)
    task22 = random_task(Task22)
    task23 = random_task(Task23)
    task24 = random_task(Task24)
    task25 = random_task(Task25)
    task26 = random_task(Task26)
    task27 = random_task(Task27)
    variant = Variant.objects.create(
        task1=task1, task2=task2, task3=task3, task4=task4, task5=task5, task6=task6,
        task7=task7, task8=task8, task9=task9, task10=task10, task11=task11, task12=task12, task13=task13,
        task14=task14,
        task15=task15, task16=task16, task17=task17, task18=task18, task19=task19, task20=task20, task21=task21,
        task22=task22, task23=task23, task24=task24, task25=task25, task26=task26, task27=task27
    )
    return variant
