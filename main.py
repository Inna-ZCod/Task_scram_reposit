import tkinter as tk
import random

# Функция добавления задач
def add_task():
    task = task_entry.get()
    if task: # если в переменной что-то есть (не пустая)
        listbox_1.insert(tk.END, task) # Добавление записи в список. Аргументы означают: добавить в конец списка и что добавить - содержимое переменной
        task_entry.delete(0, tk.END) # очистка поля ввода. Аргументы: от первого символа до конца

# Функция для перемещения задачи
def drag_task():
    l = root.focus_get() # Определяем, какому виджету принадлежит фокус
    # Если фокус у первого списка
    if l == listbox_1:
        selected_task = listbox_1.curselection() # Получаем индекс выделенного элемента
        if selected_task:
            # Получаем текст выделенного элемента
            task = listbox_1.get(selected_task)
            # Удаляем задачу из первого списка
            listbox_1.delete(selected_task)
            # Добавляем задачу в список 2 (задачи в процессе)
            listbox_2.insert(tk.END, task)
        else:
            return
    # Если фокус у второго списка
    elif l == listbox_2:
        selected_task = listbox_2.curselection() # Получаем индекс выделенного элемента
        if selected_task:
            # Получаем текст выделенного элемента
            task = listbox_2.get(selected_task)
            # Удаляем задачу из второго списка
            listbox_2.delete(selected_task)
            # Добавляем задачу в список 3 (выполненные задачи)
            listbox_3.insert(tk.END, task)
        else:
            return
    else:
        return

# Функция для удаления задач
def delet_task():
    l = root.focus_get()  # Определяем, какому виджету принадлежит фокус
    # Если фокус у первого списка
    if l == listbox_1:
        selected_task = listbox_1.curselection()  # Получаем индекс выделенного элемента
        if selected_task:
            # Удаляем задачу из первого списка
            listbox_1.delete(selected_task)
        else:
            return
    # Если фокус у второго списка
    elif l == listbox_2:
        selected_task = listbox_2.curselection() # Получаем индекс выделенного элемента
        if selected_task:
            # Удаляем задачу из второго списка
            listbox_2.delete(selected_task)
        else:
            return
    # Если фокус у третьего списка
    elif l == listbox_3:
        selected_task = listbox_3.curselection() # Получаем индекс выделенного элемента
        if selected_task:
            # Удаляем задачу из второго списка
            listbox_3.delete(selected_task)
        else:
            return
    else:
        return

# Главное окно
root = tk.Tk()
root.title("Список задач")
root.configure(background="AntiqueWhite2")
root.geometry("900x350")
root.resizable(width=False, height=False)

# Настройка главного окна
num_rows = 9  # Замените на ваше количество строк
num_columns = 4  # Замените на ваше количество столбцов

for i in range(num_rows):
    root.grid_rowconfigure(i, weight=1)

for j in range(num_columns):
    root.grid_columnconfigure(j, weight=1)

# Пустой блок (место вверху экрана)
label_0 = tk.Label(root, text="", bg="AntiqueWhite2")
label_0.grid(row=0, column=0, columnspan=3)

# Хранилище текстов для слогана
text_slogan = ["Большие дела начинаются с маленьких шагов", "Время — это то, что мы хотим больше всего, но используем хуже всего", "Действие — ключ к любому успеху", "Кто хочет - ищет возможности; кто не хочет — ищет причины", "Успех — это сумма маленьких усилий, повторяющихся день за днем", "Лучше сделать меньше, но качественно, чем много, но небрежно", "Работа, выполненная с радостью, приносит двойной результат", "Сегодняшняя работа — это завтрашний успех", "Секрет успеха — это постоянство цели", "Время, потраченное на планирование, экономит время выполнения", "Не мечтай о результате, работай над ним", "Каждый день — это новая возможность изменить свою жизнь", "Можно найти тысячу оправданий, но лучше найти один способ", "Не бойся больших задач, бойся маленьких целей"]
t_slogan = random.choice(text_slogan)

# Слоган
slogan = tk.Label(root, text=t_slogan, bg="AntiqueWhite2")
slogan.grid(row=1, column=1, columnspan=3)

# Пустой блок (между слоганом и названиями столбцов)
label_1_2 = tk.Label(root, text="", bg="AntiqueWhite2")
label_1_2.grid(row=2, column=0, columnspan=3)

# Первый блок - не начатые задачи + добавление задач
label_1 = tk.Label(root, text="Не начато", bg="AntiqueWhite2")
label_1.grid(row=3, column=1)

listbox_1 = tk.Listbox(root, width=50, bg="AntiqueWhite3")
listbox_1.grid(row=4, column=1)

# Пустой блок (между столбцами и полем для ввода задач)
label_1_3 = tk.Label(root, text="", bg="AntiqueWhite2")
label_1_3.grid(row=5, column=0, columnspan=3)

# Поле для ввода задач
task_entry = tk.Entry(root, bg="AntiqueWhite3")
task_entry.grid(row=6, column=1)
task_entry.bind("<Return>", lambda event: add_task()) # добавляем вызов функции при нажатии клавиши Enter

# Пустой блок (перед кнопками)
label_1_4 = tk.Label(root, text="", bg="AntiqueWhite2")
label_1_4.grid(row=7, column=0, columnspan=3)

# Кнопка "добавить задачу"
button_1 = tk.Button(root, text="Добавить задачу", command=add_task)
button_1.grid(row=8, column=1)

# Второй блок - задачи в процессе + перемещение задач
label_2 = tk.Label(root, text="В работе", bg="AntiqueWhite2")
label_2.grid(row=3, column=2)

listbox_2 = tk.Listbox(root, width=50, bg="AntiqueWhite3")
listbox_2.grid(row=4, column=2)

button_2 = tk.Button(root, text="Переместить задачу >>", command=drag_task)
button_2.grid(row=8, column=2)

# Третий блок - завершенные задачи + удаление задач
label_3 = tk.Label(root, text="Готово!", bg="AntiqueWhite2")
label_3.grid(row=3, column=3)

listbox_3 = tk.Listbox(root, width=50, bg="AntiqueWhite3")
listbox_3.grid(row=4, column=3)

button_3 = tk.Button(root, text="Удалить задачу", command=delet_task)
button_3.grid(row=8, column=3)

# Пустой блок (место внизу экрана)
label_4 = tk.Label(root, text="", bg="AntiqueWhite2")
label_4.grid(row=9, column=0, columnspan=3)

root.mainloop()
