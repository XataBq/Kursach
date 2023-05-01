from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Variant, all_models
from .generate_task import new_variant
from .forms import VarForm, AnswerForm, TaskForm
from .select_task_funcs import selected_tasks_into_16, selected_tasks_converter_back


# Create your views here.

def index(request):
    # global variant, select_tasks
    if request.method == 'POST':
        form = VarForm(request.POST)
        form2 = TaskForm(request.POST)
        if form.is_valid():
            if form2.is_valid():
                selected_tasks = selected_tasks_into_16(form2.cleaned_data)
                if form.cleaned_data['variant']:
                    return HttpResponseRedirect(
                        reverse('ready_var', kwargs={"pk": form.cleaned_data['variant'], "select": selected_tasks},))
                else:
                    selected_tasks = selected_tasks_into_16(form2.cleaned_data)
                    return HttpResponseRedirect(reverse('gen', kwargs={"select": selected_tasks}))
    else:
        form = VarForm()
        select_tasks = TaskForm()
    return render(request, 'generator/index.html', {"form": form, "select_form": select_tasks})


def gen(request, select):
    selected_tasks = selected_tasks_converter_back(select)
    # variant = Variant.objects.get(pk=1)
    if request.method == 'POST':
        answer_form = AnswerForm(request.POST)
        if answer_form.is_valid():
            answers = answer_form.cleaned_data
            for key in answers:
                if answers[key] == '':
                    answers[key] = 'None'
            context = {'variant': new_variant, 'answers': answers}
            if request.user.is_authenticated:
                return render(request, 'generator/answer.html', context)
            else:
                redirect('/admin/')
    else:
        answer_form = AnswerForm()
    context = {'variant': new_variant(), 'form': answer_form, 'selected_tasks': selected_tasks}
    return render(request, 'generator/gen.html', context)


def ready_var(request, pk, select, answer="On"):
    variant = Variant.objects.get(pk=pk)
    selected_tasks = selected_tasks_converter_back(select)

    if request.method == 'POST':
        # form = AnswerForm(request.POST)
        # if form.is_valid():
        #     answers = form.cleaned_data
        #     for key in answers:
        #         if answers[key] == '':
        #             answers[key] = 'None'
          pass
    else:
        form = AnswerForm()
    context = {'variant': variant, 'form': form, 'selected_tasks': selected_tasks}
    return render(request, 'generator/ready_var.html', context)


def get_task(request, num):
    tasks = all_models[num].objects.all()
    all_tasks = {}
    counter = 0
    for i in tasks:
        counter += 1
        all_tasks[f"task{counter}"] = i
    context = {'tasks': all_tasks}
    return render(request, 'generator/task.html', context)
