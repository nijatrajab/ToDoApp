from unittest import TestCase
from django.test import Client

from core.models import Todo, Task
from django.urls import reverse


def add_task_helper(client):
    return client.post(reverse("core:add_task"), {'task_value': 'Sample task'},
                       HTTP_ACCEPT='application/json')


def remove_task_helper(client, task_id):
    return client.post(reverse("core:remove_task"), {'task_id': task_id},
                       HTTP_ACCEPT='application/json')


def remove_all_task_helper(client):
    return client.post(reverse("core:remove_all_tasks"),
                       HTTP_ACCEPT='application/json')


def check_task_helper(client, task_id):
    return client.post(reverse("core:check_task"), {'task_id': task_id},
                       HTTP_ACCEPT='application/json')


def check_all_task_helper(client, task_checked):
    return client.post(reverse("core:check_all_tasks"), {'tasks_checked': task_checked},
                       HTTP_ACCEPT='application/json')


def remove_all_checked_task_helper(client):
    return client.post(reverse("core:remove_all_checked_tasks"),
                       HTTP_ACCEPT='application/json')


class TestToDo(TestCase):
    def setUp(self):
        self.client = Client()

    def test_session_data_empty(self):
        result = self.client.get('/')
        session = self.client.session

        self.assertEqual(result.status_code, 200)
        with self.assertRaises(KeyError):
            session['todo_id']

    def test_session_data_not_empty(self):
        session_before = self.client.session
        result = add_task_helper(self.client)
        session_after = self.client.session

        self.assertEqual(result.status_code, 200)
        with self.assertRaises(KeyError):
            session_before['todo_id']
        self.assertIsNotNone(session_after['todo_id'])

    def test_session_flush(self):
        add_task_helper(self.client)
        session_befero = self.client.session
        todo_id_before = session_befero['todo_id']
        session_befero.flush()

        add_task_helper(self.client)
        session_after = self.client.session
        todo_id_after = session_after['todo_id']

        self.assertNotEqual(todo_id_before, todo_id_after)

    def test_session_add_task(self):
        result = add_task_helper(self.client)
        session = self.client.session

        task = Task.objects.get(id=result.json()['task_id'])
        todo = Todo.objects.get(id=session['todo_id'])
        tasks = todo.task.all()

        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.json()['response'], 'Successfully added task.')
        self.assertEqual(result.json()['task_title'], 'Sample task')
        self.assertEqual(result.json()['task_checked'], False)
        self.assertIn(task, tasks)

    def test_session_remove_task(self):
        add_res = add_task_helper(self.client)
        session = self.client.session

        task = Task.objects.get(id=add_res.json()['task_id'])
        todo = Todo.objects.get(id=session['todo_id'])

        del_res = remove_task_helper(self.client, task.id)

        tasks = todo.task.all()

        self.assertEqual(del_res.status_code, 200)
        self.assertEqual(del_res.json()['response'], 'Successfully removed task.')
        self.assertNotIn(task, tasks)

    def test_session_check_task(self):
        add_res = add_task_helper(self.client)
        task_id = add_res.json()['task_id']
        task = Task.objects.get(id=task_id)
        check_res = check_task_helper(self.client, task.id)
        task.refresh_from_db()

        self.assertEqual(check_res.status_code, 200)
        self.assertEqual(check_res.json()['response'], 'Successfully ch task.')
        self.assertTrue(task.checked)

        check_task_helper(self.client, task.id)
        task.refresh_from_db()

        self.assertFalse(task.checked)

    def test_session_check_all_task(self):
        for i in range(5):
            add_task_helper(self.client)

        session_todo = self.client.session['todo_id']
        todo = Todo.objects.get(id=session_todo)
        check_all = check_all_task_helper(self.client, 'checked')
        todo.refresh_from_db()
        checked_tasks = todo.task.filter(checked=False)

        self.assertEqual(check_all.status_code, 200)
        self.assertEqual(check_all.json()['response'], 'Successfully ch all task.')
        self.assertEqual(5, len(checked_tasks))

        check_all_task_helper(self.client, 'unchecked')
        todo.refresh_from_db()
        checked_tasks = todo.task.filter(checked=True)

        self.assertEqual(5, len(checked_tasks))

    def test_session_remove_all_task(self):
        for i in range(5):
            add_task_helper(self.client)

        session_todo = self.client.session['todo_id']
        todo = Todo.objects.get(id=session_todo)

        self.assertEqual(5, len(todo.task.all()))

        remove_all = remove_all_task_helper(self.client)
        todo.refresh_from_db()

        self.assertEqual(remove_all.status_code, 200)
        self.assertEqual(remove_all.json()['response'], 'Successfully removed all tasks.')
        self.assertEqual(0, len(todo.task.all()))

    def test_session_remove_all_checked_task(self):
        for i in range(5):
            add_task_helper(self.client)

        session_todo = self.client.session['todo_id']
        todo = Todo.objects.get(id=session_todo)

        for i in range(3):
            check_task_helper(self.client, todo.task.all()[i].id)

        self.assertEqual(5, len(todo.task.all()))

        remove_all = remove_all_checked_task_helper(self.client)
        todo.refresh_from_db()

        self.assertEqual(remove_all.status_code, 200)
        self.assertEqual(remove_all.json()['response'], 'Successfully removed all checked tasks.')
        self.assertEqual(2, len(todo.task.all()))
