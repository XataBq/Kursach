def selected_tasks_into_16(cleaned_data):
    # преобразуем выбранные задания формы TaskForm в 16 число для передачи через url
    double_str = ''

    for key, value in cleaned_data.items():
        if value:
            double_str += '1'
        else:
            double_str += '0'

    double_str = int(double_str, 2)
    double_str = hex(double_str)

    return str(double_str)[2:]


def selected_tasks_converter_back(select):
    # функция обратная select_tasks_into_16
    selected_tasks = {}
    select = int(select, 16)
    select = str(bin(select))
    select = select[2:]
    if len(select) != 27:
        a = 27 - len(select)
        select = '0' * a + select

    for j in range(27):
        if select[j] == '1':
            selected_tasks[f"task{j + 1}"] = True
        else:
            selected_tasks[f"task{j + 1}"] = False

    return selected_tasks
