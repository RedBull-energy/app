import re
# import re for regular expression
import subprocess
import sys
# import subprocess and sys for open file
from tkinter import *
from tkinter import ttk

# import tkinter for create window app

root = Tk()
root.title("text analysis")
root.geometry("600x500")
# create basic window for our app

choice_text = ["Соня", "Другое"]
text = ""
txt = ""
entry_symbol = ""
entry_count = ""
entry_letters = ""
choice_symbol = ""
text_symbol = ""
count_space = 0


# create global var for using in function


def choice_text_for_replacement():
    global choice_text_var, text, entry_letters, entry_count, choice_symbol, txt, entry_symbol, text_symbol

    if choice_text_var.get() == "Соня":
        with open("Соня.txt", "r", encoding="utf-8") as file:
            text = file.read()
            txt = "Соня_шифр.txt"
            text_symbol = text
            # if this condition true, open Sony text file

    else:
        with open("текст.txt", "w", encoding="utf-8") as f:
            f.write("")
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, 'текст.txt'])
        txt = "текст.txt"

        # if condition false open new file for write text

        def text_1():
            global text, text_symbol
            with open("текст.txt", "r", encoding="utf-8") as file:
                text = file.read()

                text_symbol = text
            # after save new file, we press the button that run function text_1()

        btn_1 = ttk.Button(text="Выбрать свое произведение", command=text_1)
        btn_1.pack(anchor=CENTER)

    def enter_entry_field():
        global entry_count, entry_symbol, entry_letters, choice_symbol

        label = ttk.Label(root, text="Количество заменяемых комбинаций:")
        label.pack(anchor=CENTER)
        entry_count = ttk.Entry()
        entry_count.pack(anchor=CENTER)

        letters = ttk.Label(root, text="Введите символы, которые хотите заменить:")
        letters.pack(anchor=CENTER)
        entry_letters = ttk.Entry()
        entry_letters.pack(anchor=CENTER)

        label_choice_symbol = ttk.Label(root, text="Введите символы, которыми хотите заменить:")
        label_choice_symbol.pack(anchor=CENTER)
        entry_symbol = ttk.Entry()
        entry_symbol.pack(anchor=CENTER)

        choice_symbol_note = ttk.Label(root, text="• Сначала введите 'U+'")
        choice_symbol_note.pack(anchor=CENTER)

        btn_replace = ttk.Button(text="Изменить", command=main)
        btn_replace.pack(anchor=CENTER)
        # this function need for choose count and other parameters

    enter_entry_field()
    # this function need for choose and save, also choose parameters


##########################################
def main():
    global text, entry_letters, entry_count, choice_symbol, txt, text_symbol, count_space
    window = Tk()
    window.title("Replacement combinations")
    window.geometry("500x500")
    # create window for show Replacement combinations

    text_symbol = re.sub("[^А-Яа-я0-9]", "", text)
    # using regular expression for clear text

    for i in text:
        if i == " ":
            count_space = count_space + 1
            # this cycle count the number of space
    label_letters = ttk.Label(window, text=f"Количество пробелов: {count_space}")
    label_letters.pack(anchor=CENTER)

    count_other_symbol = len(text) - count_space - len(text_symbol)
    # count the number of other symbol
    label_letters = ttk.Label(window, text=f"Количество знаков препинания: {count_other_symbol}")
    label_letters.pack(anchor=CENTER)

    var = int(entry_count.get())

    let = entry_letters.get().split(",")

    choice_symbol = entry_symbol.get().split(",")

    for i in range(var):
        # cycle for replace symbol
        let_upper = let[0]
        # transfer first list value new var
        percent = 0
        percent_1 = 0
        count = 0
        count_1 = 0

        for item in range(2):
            # cycle check lowercase and uppercase symbol
            text_count = len(text_symbol)
            count = text.count(let_upper)
            print(count)
            count_1 += count
            try:
                percent = (count / text_count) * 100
                percent_1 += percent
                print(percent_1)
            except ZeroDivisionError:
                label_letters = ttk.Label(root, text=f"'Нажмите кнопку Выбрать свое произведение'")
                label_letters.pack(anchor=CENTER)

                # if user don't choose text print exception

            text = text.replace(let_upper, choice_symbol[0])
            # this method replace first symbol on second symbol
            let_upper = let_upper.title()

        label_letters = ttk.Label(window,
                                  text=f"Примерный процент замененных комбинаций '{let_upper}': {round(percent_1, 2)}%")
        label_letters.pack(anchor=CENTER)

        label_count = ttk.Label(window, text=f'Количество замененных комбинаций "{let_upper}": {count_1}')
        label_count.pack(anchor=CENTER)

        let.remove(let[0])
        # delete first value in list named let, because we are using only first value
        choice_symbol.remove(choice_symbol[0])

    def count_letters():

        window_1 = Tk()
        window_1.title("percentage of letters")
        lowFrame = Frame(window_1)
        lowFrame.grid(row=1, column=3)
        # create new grid window for show percent letters

        canvas = Canvas(lowFrame)
        frame = Frame(canvas)
        myscrollbar = Scrollbar(lowFrame, orient='vertical', command=canvas.yview)
        canvas.configure(yscrollcommand=myscrollbar.set)
        myscrollbar.pack(side='right', fill=Y)
        canvas.pack(side='left')
        canvas.create_window((0, 0), window=frame, anchor='nw')

        def conf(event):
            canvas.configure(scrollregion=canvas.bbox('all'))

        frame.bind('<Configure>', conf)
        # create scrollbar, because not all values fit into window

        seen = ""
        count_for_print = 0
        for c in text_symbol:
            if c not in seen:
                seen += c
                count_for_print += 1
                text_cont_1 = text_symbol.count(c)

                percent_letters = (text_cont_1 / text_count) * 100

                lbl = Button(frame, text=f"{c}: {round(percent_letters, 2)}%")
                lbl.grid(row=count_for_print, column=0)
            # cycle show percent letters

    with open(txt, "w") as file:
        text = file.write(text)
        # text with replacement write in file

    btn = ttk.Button(text="Рассчитать процент букв", command=count_letters)
    btn.pack(anchor=CENTER)

    label_count = ttk.Label(root, text=f'Ваш текст сохранен')
    label_count.pack(anchor=CENTER)

    def opener_text():

        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, txt])

    btn = ttk.Button(text="Показать произведение", command=opener_text)
    btn.pack(anchor=CENTER)
    # if we want to see text work function opener_text


choice_text_var = StringVar(value=choice_text[0])
combobox = ttk.Combobox(textvariable=choice_text_var, values=choice_text)
combobox.pack(anchor=CENTER)

btn = ttk.Button(text="Выбрать", command=choice_text_for_replacement)
btn.pack(anchor=CENTER)

root.mainloop()
