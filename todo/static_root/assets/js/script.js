function taskItem(taskID, taskTitle, isNew, isChecked) {
    const taskValue = document.getElementById("id_task_list")
    const todoDiv = document.createElement("div")
    todoDiv.classList.add("todo-list")
    todoDiv.style.opacity = '0'
    todoDiv.style.height = '0px'
    todoDiv.id = 'id_todo_' + taskID

    const todoA = document.createElement("a")
    todoA.classList.add('task-list-item')
    todoA.id = "id_task_item_" + taskID
    todoA.innerHTML = taskTitle
    if (isChecked) {
        todoA.style.textDecorationLine = 'line-through';
    }
    todoDiv.appendChild(todoA)

    const todoCheck = document.createElement("button")
    if (isNew) {
        todoCheck.classList.add("task-list-check", "faa-parent", "animated-hover")
    } else {
        if (isChecked) {
            todoCheck.classList.add("task-list-uncheck", "faa-parent", "animated-hover")
        } else {
            todoCheck.classList.add("task-list-check", "faa-parent", "animated-hover")
        }
    }
    todoCheck.type = 'button'
    todoCheck.id = "id_task_check_" + taskID
    todoCheck.onclick = function () {
        checkTask(taskID, taskTitle)
    }

    const todoCheckIcon = document.createElement("i")
    if (isNew) {
        todoCheckIcon.classList.add("fas", "fa-check", "faa-horizontal", "faa-reverse")
    } else {
        if (isChecked) {
            todoCheckIcon.classList.add("fas", "fa-undo-alt", "faa-wrench", "faa-fast")
        } else {
            todoCheckIcon.classList.add("fas", "fa-check", "faa-horizontal", "faa-reverse")
        }
    }
    todoCheck.appendChild(todoCheckIcon)
    todoDiv.appendChild(todoCheck)

    const todoRemove = document.createElement("button")
    todoRemove.classList.add("task-list-remove", "faa-parent", "animated-hover")
    todoRemove.type = 'button'
    todoRemove.id = "id_task_remove_" + taskID
    todoRemove.onclick = function () {
        removeTask(taskID)
    }

    const todoRemoveIcon = document.createElement("i")
    todoRemoveIcon.classList.add("far", "fa-trash-alt", "faa-flash", "faa-fast")
    todoRemove.appendChild(todoRemoveIcon)
    todoDiv.appendChild(todoRemove)

    if (isNew) {
        taskValue.insertBefore(todoDiv, taskValue.childNodes[0])
        $('#id_todo_' + taskID).animate({height: '58px'}, 150, function () {
            $('#id_todo_' + taskID).animate({opacity: '1'}, 150)
        })
    } else {
        if (isChecked) {
            if ($('.task-list-uncheck:first').parents()[0]) {
                taskValue.insertBefore(todoDiv, $('.task-list-uncheck:first').parents()[0])
            } else {
                taskValue.insertBefore(todoDiv, taskValue.lastChild)
            }
            $('#id_todo_' + taskID).animate({height: '58px'}, 150, function () {
                $('#id_todo_' + taskID).animate({opacity: '1'}, 150)
            })
        } else {
            if ($('.task-list-check:last').parents()[0]) {
                taskValue.insertBefore(todoDiv, $('.task-list-check:last').parents()[0].nextSibling)
            } else {
                taskValue.insertBefore(todoDiv, taskValue.childNodes[0])
            }
            $('#id_todo_' + taskID).animate({height: '58px'}, 150, function () {
                $('#id_todo_' + taskID).animate({opacity: '1'}, 150)
            })
        }

    }

}

function taskCheckButton(taskID, taskTitle) {
    const taskButton = document.getElementById("id_task_check_" + taskID)
    const taskA = document.getElementById("id_task_item_" + taskID)
    const taskCheckAllButton = document.getElementById("id_check_all")
    if (taskButton.classList.contains('task-list-check')) {
        taskButton.classList.remove('task-list-check');
        taskButton.classList.add('task-list-uncheck');
        taskButton.children[0].classList.remove('fa-check', "faa-horizontal", "faa-reverse")
        taskButton.children[0].classList.add('fa-undo-alt', "faa-wrench", "faa-fast")
        taskA.style.textDecorationLine = 'line-through'
        taskRemoveButton(taskID, true)
        setTimeout(() => {
            taskItem(taskID, taskTitle, false, true)
        }, 400);
        if (document.querySelectorAll(".task-list-check").length === 0) {
            taskCheckAllButton.innerHTML = "Uncheck all tasks"
            taskCheckAllButton.classList.remove('check-all')
            taskCheckAllButton.classList.add('uncheck-all')
        } else {
            taskCheckAllButton.innerHTML = "Check all tasks"
            taskCheckAllButton.classList.remove('uncheck-all')
            taskCheckAllButton.classList.add('check-all')
        }
    } else if (taskButton.classList.contains('task-list-uncheck')) {
        taskButton.classList.remove('task-list-uncheck');
        taskButton.classList.add('task-list-check');
        taskButton.children[0].classList.remove('fa-undo-alt', "faa-wrench", "faa-fast")
        taskButton.children[0].classList.add('fa-check', "faa-horizontal", "faa-reverse")
        taskA.style.textDecorationLine = 'none'
        taskRemoveButton(taskID, true)
        setTimeout(() => {
            taskItem(taskID, taskTitle, false, false)
        }, 400);
        if (document.querySelectorAll(".task-list-check").length !== 0) {
            taskCheckAllButton.innerHTML = "Check all tasks"
            taskCheckAllButton.classList.remove('uncheck-all')
            taskCheckAllButton.classList.add('check-all')
        } else {
            taskCheckAllButton.innerHTML = "Uncheck all tasks"
            taskCheckAllButton.classList.remove('check-all')
            taskCheckAllButton.classList.add('uncheck-all')
        }
    }
}

function taskCheckAll() {
    const taskButtonsChecked = document.querySelectorAll(".task-list-check")
    const taskButtonsUnchecked = document.querySelectorAll(".task-list-uncheck")
    const taskCheckAllButton = document.getElementById("id_check_all")
    // const allButton = document.getElementById("id_remove_checked_all")
    if (taskButtonsChecked.length == 0) {
        taskButtonsUnchecked.forEach(function (el) {
            el.classList.remove('task-list-uncheck');
            el.classList.add('task-list-check');
            el.children[0].classList.remove('fa-undo-alt', "faa-wrench", "faa-fast")
            el.children[0].classList.add('fa-check', "faa-horizontal", "faa-reverse")
        });
        taskCheckAllButton.innerHTML = "Check all tasks"
        taskCheckAllButton.classList.remove('uncheck-all')
        taskCheckAllButton.classList.add('check-all')
    } else if (taskButtonsUnchecked.length == 0) {
        taskButtonsChecked.forEach(function (el) {
            el.classList.remove('task-list-check');
            el.classList.add('task-list-uncheck');
            el.children[0].classList.remove('fa-check', "faa-horizontal", "faa-reverse")
            el.children[0].classList.add('fa-undo-alt', "faa-wrench", "faa-fast")
        });
        taskCheckAllButton.innerHTML = "Uncheck all tasks"
        taskCheckAllButton.classList.remove('check-all')
        taskCheckAllButton.classList.add('uncheck-all')
    } else {
        taskButtonsChecked.forEach(function (el) {
            el.classList.remove('task-list-check');
            el.classList.add('task-list-uncheck');
            el.children[0].classList.remove('fa-check', "faa-horizontal", "faa-reverse")
            el.children[0].classList.add('fa-undo-alt', "faa-wrench", "faa-fast")
        });
        taskCheckAllButton.innerHTML = "Uncheck all tasks"
        taskCheckAllButton.classList.remove('check-all')
        taskCheckAllButton.classList.add('uncheck-all')
    }
}

function taskRemoveButton(taskID, isCheck) {
    const taskItem = $('#id_todo_' + taskID)
    const allButton = document.getElementById("all_buttons")
    const taskCheckAllButton = document.getElementById("id_check_all")
    taskItem.animate({opacity: '0'}, 150, function () {
        taskItem.animate({height: '0'}, 150, function () {
            taskItem.remove()
            if (!isCheck) {
                if (document.querySelectorAll(".todo-list").length === 0) {
                    allButton.classList.remove('all-buttons')
                    allButton.classList.add('all-buttons-hide')
                    taskCheckAllButton.innerHTML = "Check all tasks"
                    taskCheckAllButton.classList.remove('uncheck-all')
                    taskCheckAllButton.classList.add('check-all')
                }
            }
        })
    })


}

function taskRemoveAll() {
    const taskItem = $('.todo-list')

    taskItem.each(function () {
        $(this).animate({opacity: '0'}, 150, function () {
            $(this).animate({height: '0'}, 150, function () {
                $(this).remove()
            })
        })
    })

}

function taskRemoveAllChecked() {
    const taskItem = $('.task-list-uncheck').parent()
    const allButton = document.getElementById("all_buttons")

    taskItem.each(function () {
        $(this).animate({opacity: '0'}, 150, function () {
            $(this).animate({height: '0'}, 150, function () {
                $(this).remove();
                if (document.querySelectorAll('.todo-list').length === 0) {
                    allButton.classList.remove('all-buttons')
                    allButton.classList.add('all-buttons-hide')
                }
            })
        })
    })

}

$("#id_task_input").keyup(function (event) {
    if (event.keyCode === 13) {
        $("#id_task_input_button").click();
    }
});

