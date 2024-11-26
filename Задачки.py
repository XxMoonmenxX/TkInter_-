from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo

click = 0
def fullsc(): # ф
    win.attributes("-fullscreen", True)
def outscrn():
    win.attributes("-fullscreen", False)
def clicker(): # добавляет +1 за клик по кнопке "click"
    global click
    click += 1
    label['text'] = f' {click}'

def ehit(): #  можно создать кнопку выхода и вставить туда комманду ehit
    win.destroy()


def finish():# функция удержания закрытия окна, чтобы можно было вставить дочернее окошко по типу "вы уверены что хотите выйти?". можно обойтись и без него
    win.destroy()
win = Tk() # создаём переменную вин и присвоим функцию нашей библиотеки
win.title('Name') # тут имя окошка пишется
win.geometry("720x480")
win.protocol('WM_DELETE_WINDOW', finish) # Протокол WM_DELETE_WINDOW в Tkinter вызывается, когда окно верхнего уровня должно уже закрываться. По умолчанию Tk уничтожает окно, для которого оно было получено. cпс яндекс нейро
win.resizable() # даёт свободно растягивать/стягивать окно

label = Label(text='цэфры')#создаёт текст посередине экрана
label.pack()

flscrn = ttk.Button(text='Во весь экран', command=fullsc) #добавляет кнопки, их название и комманды к кнопкам, отзывает к функциям def
flscrn.place(x=10,y=0)# расположение кнопок
outscrn = ttk.Button(text='В окне', command=outscrn)
outscrn.place(x=10,y=21)
clickk = ttk.Button(text='click', command=clicker)
clickk.place(x=10, y=42)
# есть функция anchor, которая тоже отвечает за расположение кнопок:n: положение вверху по центру
# e: положение в правой части контейнера по центру
# s: положение внизу по центру
# w: положение в левой части контейнера по центру
# nw: положение в верхнем левом углу
# ne: положение в верхнем правом углу
# se: положение в нижнем правом углу
# sw: положение в нижнем левом углу
# center: положение центру
# к примеру:
# button = ttk.Button()
# button.place(anchor = 'center')
# Параметры height и width устанавливают соответственно высоту и ширину элемента в пикселях:
# button = ttk.Button()
# button.place(anchor = 'center',widht = 80, height = 100)
# Параметры relheight и relwidth используют float, тобиш 80.1 или 100.324
# питон не признаёт запятых!!! только точка во float!


def print_info(widget, depth=0): # поиск кнопок по координатам, взято из инета
    widget_class = widget.winfo_class()
    widget_width = widget.winfo_width()
    widget_height = widget.winfo_height()
    widget_x = widget.winfo_x()
    widget_y = widget.winfo_y()
    print("   " * depth + f"{widget_class} width={widget_width} height={widget_height}  x={widget_x} y={widget_y}")
    for child in widget.winfo_children():
        print_info(child, depth + 1)

#добавим поле ввода, кнопку и чтение данных при нажатии кнопки и вывода данных в Label
def vnesti():#создаем функцию
    vivod['text'] = pole_vvoda.get()#переменныя "вывод" равная полю ввода, тоесть то, что мы ввели в поле воода. да. вот так.
def sbros():# функция сброса, ну как... костыль. просто даем переменным те значения, которые у них были
    pole_vvoda.delete(0, END)
    vivod['text'] = ''
    label['text'] = 'цэфры'

pole_vvoda = ttk.Entry() # пришли к созданию поля ввода Ентри эт поле ввода
pole_vvoda.place(x=10, y=63) # расположение поля ввода
knopka = ttk.Button(text='Внести данные', command=vnesti) # кнопошка с коммандой
knopka.place(x=10,y=84)
vivod = ttk.Label() # создаем просто текстовое поле, а даём туда инфу в функции "Внести" выше.
vivod.place(x=10, y=110)
knopka_sbrosa = ttk.Button(text='Сбросить', command=sbros) # та самая кнопошка сброса
knopka_sbrosa.place(x=10,y=125)

#добавим простейшую аутентификацию
#создадим переменную пароль
password = 1234
#мы замечательны
#начинаем создавать функцию проверки пароля
def chekpass():
    global password #объявляем эту переменную в функции
    if passchek.get() == str(password): #проверяем соответсвует поле ввода паролю или нет. Делаем переменную пароля строчной, а то не заработает.
        infa['text'] = 'вы ввели пароль правильно'# все ок и происходит действие что пароль верный
    else:
        infa['text'] = 'вы ввели пароль неправильно'# все не ок, происходит действие что пароль не верный

infa = Label(text='Введите пароль')#создаем текстовое поле
infa.place(x=10, y=150 )
passchek = ttk.Entry()#создаем поле ввода
passchek.place(x=10,y=175)
buttomapss = ttk.Button(text='Ввести пароль', command=chekpass) #создаем кнопку проверки пароля
buttomapss.place(x=10, y=200)

#Добавим галочку
def Galka(): # функция галочки
    if enabled.get() == 1: # условия проверки нажатия на галочку ( true или false; 1 или 0).
        showinfo(title="Info", message="Второе окно создано.") # из подллибы showinfo
        ## докидаем сюда ещё функции для галки.
        tk = Tk() # определяем переменную дял окна
        tk.title('Окно 2') # Даем название
        tk.geometry("360x480")# Даем размер
        info = Label(tk,text='Окно два')# вывод текста во втором окне
        info.place(x=10, y= 10)# местоположение текста
        tk.mainloop()# луп окна
    else: # если enabled.get() = 0
        showinfo(title="Info", message="Зачем?") # Удаляем новое окошко



enabled = IntVar() # создание виджета с галочкой

enabled_checkbutton = ttk.Checkbutton(text="Галка", variable=enabled, command=Galka) # variable - значение галки 1 или 0.
enabled_checkbutton.place(x=10, y=230)
# можно сделать дохера галок с разными названиями/
# Можно добавить разный текст на состояние галки
# вот пример кода:
# enabled_on = "Включено"
# enabled_off = "Отключено"
# enabled = StringVar(value=enabled_on)
#
# enabled_checkbutton = ttk.Checkbutton(textvariable=enabled, variable=enabled, offvalue=enabled_off, onvalue=enabled_on)

win.update()  # обновляем информацию о виджетах

print_info(win)


win.mainloop() # луп окна, чтобы не закрывалось