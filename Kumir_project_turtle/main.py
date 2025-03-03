import tkinter as tk
from turtle import RawTurtle, TurtleScreen, ScrolledCanvas

# Глобальные переменные
scale_factor = 10  # Масштаб для движения черепахи


# Функция для выполнения команд черепахи
def execute_commands():
    # Очищаем поле ошибок
    error_label.config(text="", fg="black")

    # Сбрасываем черепаху в начальное положение и очищаем рисунок
    turtle.reset()
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.pensize(3)  # Увеличиваем толщину линии

    commands = command_entry.get("1.0", tk.END).strip().splitlines()  # Получаем команды из текстового поля
    i = 0
    in_algorithm = False  # Флаг для проверки, что есть "алг" и "нач"
    in_loop = False  # Флаг для проверки, что есть "нц" и "кц"
    loop_stack = []  # Стек для вложенных циклов

    try:
        while i < len(commands):
            cmd = commands[i].strip()
            if not cmd:  # Пропускаем пустые строки
                i += 1
                continue

            if cmd.startswith("алг"):
                in_algorithm = True
                i += 1
            elif cmd.startswith("нач"):
                if not in_algorithm:
                    raise SyntaxError("Отсутствует 'алг' перед 'нач'")
                i += 1
            elif cmd.startswith("кон"):
                if not in_algorithm:
                    raise SyntaxError("Отсутствует 'алг' перед 'кон'")
                in_algorithm = False
                i += 1
            elif cmd.startswith("нц"):
                if not in_algorithm:
                    raise SyntaxError("Команды должны быть внутри 'алг' и 'нач'")
                try:
                    repeat_count = int(cmd[3:].split("раз")[0].strip())  # Получаем количество повторений
                    loop_stack.append((i + 1, repeat_count))  # Запоминаем начало цикла и количество повторений
                    in_loop = True
                except (IndexError, ValueError):
                    raise SyntaxError("Некорректный формат цикла 'нц'")
                i += 1
            elif cmd.startswith("кц"):
                if not in_loop:
                    raise SyntaxError("Отсутствует 'нц' перед 'кц'")
                start_index, repeat_count = loop_stack.pop()
                if repeat_count > 1:
                    loop_stack.append((start_index, repeat_count - 1))  # Уменьшаем количество повторений
                    i = start_index  # Возвращаемся к началу цикла
                else:
                    in_loop = False
                    i += 1
            else:
                if not in_algorithm:
                    raise SyntaxError("Команды должны быть внутри 'алг' и 'нач'")
                execute_single_command(cmd)
                i += 1

        if in_algorithm:
            raise SyntaxError("Отсутствует 'кон'")
        if in_loop:
            raise SyntaxError("Отсутствует 'кц'")

    except SyntaxError as e:
        error_label.config(text=f"Ошибка: {e}", fg="red")
    except Exception as e:
        error_label.config(text=f"Ошибка: {e}", fg="red")


# Функция для выполнения одной команды
def execute_single_command(cmd):
    try:
        if cmd.startswith("вперед(") and cmd.endswith(")"):
            distance = int(cmd[7:-1]) * scale_factor  # Умножаем на масштаб
            turtle.forward(distance)
        elif cmd.startswith("вправо(") and cmd.endswith(")"):
            angle = int(cmd[7:-1])
            turtle.right(angle)
        elif cmd.startswith("влево(") and cmd.endswith(")"):
            angle = int(cmd[6:-1])
            turtle.left(angle)
        elif cmd == "поднять хвост":
            turtle.penup()
        elif cmd == "опустить хвост":
            turtle.pendown()
        else:
            raise SyntaxError(f"Неизвестная команда: {cmd}")
    except (IndexError, ValueError):
        raise SyntaxError(f"Некорректная команда: {cmd}")


# Функция для рисования сетки
def draw_grid():
    grid_turtle = RawTurtle(screen)
    grid_turtle.hideturtle()
    grid_turtle.speed(0)
    grid_turtle.penup()

    # Рисуем серую сетку
    grid_turtle.color("gray")
    for x in range(-500, 501, 50):
        grid_turtle.goto(x, -500)
        grid_turtle.pendown()
        grid_turtle.goto(x, 500)
        grid_turtle.penup()
    for y in range(-500, 501, 50):
        grid_turtle.goto(-500, y)
        grid_turtle.pendown()
        grid_turtle.goto(500, y)
        grid_turtle.penup()

    # Рисуем коричневые оси X и Y
    grid_turtle.color("brown")
    grid_turtle.goto(-500, 0)
    grid_turtle.pendown()
    grid_turtle.goto(500, 0)
    grid_turtle.penup()
    grid_turtle.goto(0, -500)
    grid_turtle.pendown()
    grid_turtle.goto(0, 500)
    grid_turtle.penup()


# Функция для изменения масштаба
def update_scale(value):
    scale = float(value) / 100
    screen.screensize(1000 * scale, 1000 * scale)
    canvas.config(scrollregion=canvas.bbox("all"))


# Создаем основное окно
root = tk.Tk()
root.title("Исполнитель Черепаха")

# Создаем холст для черепахи
canvas = ScrolledCanvas(root, width=500, height=500)
canvas.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
canvas.config(bg="yellow")  # Устанавливаем цвет фона

# Создаем экран для черепахи
screen = TurtleScreen(canvas)
turtle = RawTurtle(screen)
turtle.shape("turtle")  # Делаем черепаху в форме черепахи
turtle.pensize(3)  # Увеличиваем толщину линии

# Рисуем сетку
draw_grid()

# Создаем поле для ввода команд
command_frame = tk.Frame(root)
command_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

command_label = tk.Label(command_frame, text="Введите команды для черепахи:")
command_label.pack()

command_entry = tk.Text(command_frame, width=40, height=20)
command_entry.pack(fill=tk.BOTH, expand=True)


# Добавляем поддержку Ctrl+V
def paste_text(event):
    command_entry.insert(tk.INSERT, root.clipboard_get())
    return "break"  # Предотвращаем стандартное поведение


command_entry.bind("<Control-v>", paste_text)

execute_button = tk.Button(command_frame, text="Выполнить", command=execute_commands)
execute_button.pack()

# Поле для вывода ошибок
error_label = tk.Label(command_frame, text="", fg="red")
error_label.pack()

# Поле для изменения масштаба
scale_label = tk.Label(command_frame, text="Масштаб (%):")
scale_label.pack()

scale_slider = tk.Scale(command_frame, from_=10, to=200, orient=tk.HORIZONTAL, command=update_scale)
scale_slider.set(100)
scale_slider.pack()


# Включаем перемещение по холсту с помощью мыши
def start_drag(event):
    canvas.scan_mark(event.x, event.y)


def drag(event):
    canvas.scan_dragto(event.x, event.y, gain=1)


canvas.bind("<ButtonPress-1>", start_drag)
canvas.bind("<B1-Motion>", drag)

# Запускаем главный цикл
root.mainloop()