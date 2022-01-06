import json

from django.http import HttpResponse
from django.shortcuts import render

from core.models import Todo, Task


def todo_list(request):
    try:
        todo_id = request.session['todo_id']
    except Exception:
        todo_id = None

    if todo_id:
        todo = Todo.objects.get(id=todo_id)
        tasks = todo.task.all().order_by('checked')
        tasks_all_checked = any(t.checked is False for t in tasks)
        context = {'todo': tasks, 'tac': tasks_all_checked}
    else:
        todo_empty = 'ToDo list is empty'
        context = {'empty': True, 'todo_empty': todo_empty}

    return render(request, 'index.html', context)


def add_task(request, *args, **kwargs):
    payload = {}

    try:
        todo_id = request.session['todo_id']
    except Exception:
        new_todo = Todo()
        new_todo.save()
        request.session['todo_id'] = new_todo.id
        todo_id = new_todo.id

    todo = Todo.objects.get(id=todo_id)
    task_value = request.POST.get("task_value")

    if task_value != "":
        task = Task.objects.create(task=task_value)
        todo.task.add(task)
        payload['task_title'] = task.task
        payload['task_id'] = task.id
        payload['task_checked'] = task.checked
        payload['response'] = "Successfully added task."
    else:
        payload['response'] = 'Task can not be empty'
    return HttpResponse(json.dumps(payload), content_type="application/json")


def remove_task(request, *args, **kwargs):
    payload = {}

    try:
        request.session['todo_id']
    except Exception:
        new_todo = Todo()
        new_todo.save()
        request.session['todo_id'] = new_todo.id

    task_value = request.POST.get("task_id")

    if task_value != "":
        try:
            task = Task.objects.get(id=task_value)
            task.delete()
            payload['response'] = "Successfully removed task."
        except Task.DoesNotExist:
            payload['response'] = "Task already have been removed."
    else:
        payload['response'] = 'Task can not be empty.'

    return HttpResponse(json.dumps(payload), content_type="application/json")


def check_task(request, *args, **kwargs):
    payload = {}

    try:
        request.session['todo_id']
    except Exception:
        new_todo = Todo()
        new_todo.save()
        request.session['todo_id'] = new_todo.id

    task_value = request.POST.get("task_id")

    if task_value != "":
        try:
            task = Task.objects.get(id=task_value)
            if task.checked:
                task.checked = False
                task.save()
                payload['response'] = "Successfully ch task."
            else:
                task.checked = True
                task.save()
                payload['response'] = "Successfully ch task."
        except Task.DoesNotExist:
            payload['response'] = "Task already have been removed."
    else:
        payload['response'] = 'Task can not be empty.'

    return HttpResponse(json.dumps(payload), content_type="application/json")


def check_all_tasks(request, *args, **kwargs):
    payload = {}

    try:
        todo_id = request.session['todo_id']
    except Exception:
        new_todo = Todo()
        new_todo.save()
        request.session['todo_id'] = new_todo.id
        todo_id = new_todo.id

    todo = Todo.objects.get(id=todo_id)
    task_value = request.POST.get("tasks_checked")
    if task_value != "":
        tasks = todo.task.all()
        if tasks:
            if task_value == "checked":
                for task in tasks:
                    task.checked = False
                    task.save()
                payload['response'] = 'Successfully ch all task.'
            elif task_value == "unchecked":
                for task in tasks:
                    task.checked = True
                    task.save()
                payload['response'] = 'Successfully ch all task.'
            payload['response'] = 'Successfully ch all task.'
        else:
            payload['response'] = "There is no task."
    else:
        payload['response'] = 'Task can not be empty.'

    return HttpResponse(json.dumps(payload), content_type="application/json")


def remove_all_tasks(request, *args, **kwargs):
    payload = {}

    try:
        todo_id = request.session['todo_id']
    except Exception:
        new_todo = Todo()
        new_todo.save()
        request.session['todo_id'] = new_todo.id
        todo_id = new_todo.id

    todo = Todo.objects.get(id=todo_id)

    tasks = todo.task.all()
    if tasks:
        tasks.delete()
        payload['response'] = 'Successfully removed all tasks.'
    else:
        payload['response'] = "There is no task."

    return HttpResponse(json.dumps(payload), content_type="application/json")


def remove_all_checked_tasks(request, *args, **kwargs):
    payload = {}

    try:
        todo_id = request.session['todo_id']
    except Exception:
        new_todo = Todo()
        new_todo.save()
        request.session['todo_id'] = new_todo.id
        todo_id = new_todo.id

    tasks = Task.objects.filter(todo__id=todo_id, checked=True)

    if tasks:
        tasks.delete()
        payload['response'] = 'Successfully removed all checked tasks.'
    else:
        payload['response'] = "There is no checked tasks."

    return HttpResponse(json.dumps(payload), content_type="application/json")
